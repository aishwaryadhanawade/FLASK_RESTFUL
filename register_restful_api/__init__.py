from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
import datetime
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
app.config['MONGO_URI']="mongodb://mongodb:27017/mdbb"
# mongo= MongoClient("mongodb://mongodb:27017/")
app.config["JWT_SECRET_KEY"] = "HS256"
JWT_ACCESS_TOKEN_TIMEDELTA = datetime.timedelta(minutes=15)
jwt = JWTManager(app)
user_collection=PyMongo(app)
# db=mongo['mdbb']
# user_collection=db['users']
