import os
from flask import Flask

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
USERAGENT = os.environ["USERAGENT"]
print("Initializing bot deployed on Heroku with user agent ", USERAGENT)
