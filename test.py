from pymongo import MongoClient
mongo= MongoClient("mongodb://mongodb:27017/mdbb")
database=mongo["mdbb"]
collectionsss=database["users"]
print(collectionsss)
data=list(collectionsss.find())
print(data)