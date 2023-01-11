from pymongo import * 

#mongo connection db
def mongo_connection():
    client = MongoClient("mongodb://localhost:27017")
    db = client.bigdata
    return db

def mongo_connection_library():
    client = MongoClient("mongodb://localhost:27017")
    db = client.bigdata
    return db.library

def mongo_connection_person():
    client = MongoClient("mongodb://localhost:27017")
    db = client.bigdata
    return db.person

def mongo_connection_books():
    client = MongoClient("mongodb://localhost:27017")
    db = client.bigdata
    return db.books

def mongo_connection_category():
    client = MongoClient("mongodb://localhost:27017")
    db = client.bigdata
    return db.category