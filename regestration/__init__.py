import datetime

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from pymongo import MongoClient
from datetime import timedelta


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "HS256"
mongo= MongoClient("mongodb://localhost:27017/")
db=mongo['mdb']

JWT_ACCESS_TOKEN_TIMEDELTA=datetime.timedelta(minutes=15)
coll=db['newcol']
jwt=JWTManager(app)
api = Api(app)

