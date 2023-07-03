from flask import Flask
from flask_restful import Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

mongo= MongoClient("mongodb://localhost:27017/")
db=mongo['mdb']
user_collection=db['users']
