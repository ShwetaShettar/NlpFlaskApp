from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "plagiarism_db"
mongo = PyMongo(app, config_prefix= 'MONGO')
APP_URL = "http://127.0.0.1:5000"

from app import views
