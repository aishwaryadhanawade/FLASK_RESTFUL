from flask import Flask
from flask_restful import Api
from pymongo import MongoClient
import datetime
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)

mongo= MongoClient("mongodb://localhost:27017/")
app.config["JWT_SECRET_KEY"] = "HS256"
JWT_ACCESS_TOKEN_TIMEDELTA = datetime.timedelta(minutes=15)
jwt = JWTManager(app)
db=mongo['mdb']
user_collection=db['users']
