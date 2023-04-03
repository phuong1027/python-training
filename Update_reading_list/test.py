from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

book_db = client["BookDB"]

print(client)