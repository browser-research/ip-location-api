from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

ENV = environ.get("ENV")
if ENV == "DEVELOPMENT":
    DEBUG = True

IP2LOCATION_TOKEN = environ.get("IP2LOCATION_TOKEN")
SECRET_KEY = environ.get("SECRET_KEY")
