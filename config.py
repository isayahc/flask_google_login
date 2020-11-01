"""Flask configuration variables."""
# This is where you can change env
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".test.env"))  # use for different .envs


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    """Set Flask configuration from .env file."""

    # General Config
    TESTING = True  # enable testing

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("TEST_SQLALCHEMY_DATABASE_URI")
