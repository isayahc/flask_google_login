from os import environ
import json

from flask import current_app as app
from flask import redirect, request, url_for, render_template

from . import db
from .model import User

from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)
from oauthlib.oauth2 import WebApplicationClient

import requests


GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")
client = WebApplicationClient(GOOGLE_CLIENT_ID)


@login_required
@app.route('/hello')
def hello():
    name = current_user.name
    return f"Hello, {name}!"


@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template('home.jinja', title='home')
    #         '<meta name="google-site-verification" content="P_wpVI14UDAjBIpaHBUyae1MXMvjsH8QKKsziBICVGE" />'
    #         "<p>Hello, {}! You're logged in! Email: {}</p>"
    #         "<div><p>Google Profile Picture:</p>"
    #         '<img src="{}" alt="Google profile pic"></img></div>'
    #         '<a class="button" href="/logout">Logout</a>'.format(
    #             current_user.name, current_user.email, current_user.profile_pic
    #         )
    #     )
    # else:
    #     return '<a class="button" href="/login">Google Login non auth g</a>'


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@app.route("/login")
def login():
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]  # unused
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    existing_user = User.query.filter(
            User.email == users_email
        ).first()

    if existing_user:
        login_user(existing_user)
        # current_user.is_authenticated = True
        return redirect(url_for(".index"))
    else:
        new_user = User(
            name=users_name,
            email=users_email,
            profile_pic=picture,
        )
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()

        login_user(new_user)
        # current_user.is_authenticated = True
        return redirect(url_for(".index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/google66a812c9d2e8e42f.html')
def tester():
    return render_template('google66a812c9d2e8e42f.html')
