import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
OAUTH_TOKEN = os.environ.get("OAUTH_TOKEN")
OAUTH_TOKEN_SECRET = os.environ.get("OAUTH_TOKEN_SECRET")
