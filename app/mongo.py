from pymongo import * 
import random
import hashlib
import os 
# DB CONNECTION -----------

#mongo connection db
def mongo_connection():
    client = MongoClient("mongodb://mongo-db:27017")
    db = client.orion
    return db

#connection to collection entities
def mongo_connection_entities():
    client = MongoClient("mongodb://mongo-db:27017")
    db = client.orion
    return db.entities

# DB OPERATION ------------
def get_seats(entitiesCollection):
    record = entitiesCollection.find( {"_id.type":"https://schema.org/Library"},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    for rec in record:
        seats = rec.get("attrs").get("https://uri=etsi=org/ngsi-ld/default-context/seats").get("value")
    return seats

def random_seats(entitiesCollection):
    record = entitiesCollection.find( {"_id.type":"https://schema.org/Library"},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    for rec in record:
        seats = rec.get("attrs").get("https://uri=etsi=org/ngsi-ld/default-context/seats").get("value")
        seats = int(seats)
    if(random.randint(0, 1) == 0):
        seats = seats + random.randint(1, 5)
    else:
        seats = seats - random.randint(1, 5)
    myquery = {"_id.id":"urn:ngsi-ld:Library:library001"}
    newvalues = { "$set": { "attrs.https://uri=etsi=org/ngsi-ld/default-context/seats.value": seats } }
    entitiesCollection.update_one(myquery, newvalues)

def change_seats(entitiesCollection,number_seats):
    record = entitiesCollection.find( {"_id.type":"https://schema.org/Library"},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    for rec in record:
        seats = rec.get("attrs").get("https://uri=etsi=org/ngsi-ld/default-context/seats").get("value")
        seats = int(seats)
    seats = seats + number_seats
    myquery = {"_id.id":"urn:ngsi-ld:Library:library001"}
    newvalues = { "$set": { "attrs.https://uri=etsi=org/ngsi-ld/default-context/seats.value": seats } }
    entitiesCollection.update_one(myquery, newvalues)

def change_book_availability(entitiesCollection,isbn):
    resultbooks = entitiesCollection.find( {"_id.type":"https://schema.org/Book","attrs.https://schema=org/isbn.value":isbn},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listBook = []
    for res in resultbooks:
        book = []
        book.append(res.get("attrs").get("https://schema=org/isbn").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/title").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/description").get("value"))
        book.append(res.get("attrs").get("https://schema=org/author").get("value"))
        book.append(res.get("attrs").get("https://uri=fiware=org/ns/data-models#category").get("value"))
        book.append(res.get("attrs").get("https://schema=org/image").get("value"))
        book.append(res.get("attrs").get("https://schema=org/value").get("value"))
        listBook.append(book)
    if (listBook[0][6] == 0):
        listBook[0][6] = 1
    else:
        listBook[0][6] = 0

    myquery = {"attrs.https://schema=org/isbn.value":isbn}
    newvalues = { "$set": { "attrs.https://schema=org/value.value": listBook[0][6] } }
    entitiesCollection.update_one(myquery, newvalues)

def list_all_category(entitiesCollection):
    resultCategory = entitiesCollection.find( {"_id.type":"https://schema.org/Category"},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listCategory = []
    for res in resultCategory:
        category = []
        category.append(res.get("attrs").get("https://schema=org/name").get("value"))
        listCategory.append(category)
    return listCategory

def list_all_books(entitiesCollection):
    resultbooks = entitiesCollection.find( {"_id.type":"https://schema.org/Book"},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listBook = []
    for res in resultbooks:
        book = []
        book.append(res.get("attrs").get("https://schema=org/isbn").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/title").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/description").get("value"))
        book.append(res.get("attrs").get("https://schema=org/author").get("value"))
        book.append(res.get("attrs").get("https://uri=fiware=org/ns/data-models#category").get("value"))
        book.append(res.get("attrs").get("https://schema=org/image").get("value"))
        book.append(res.get("attrs").get("https://schema=org/value").get("value"))
        listBook.append(book)
    return listBook

def list_all_books_filtered_by_available(entitiesCollection,available):
    resultbooks = entitiesCollection.find( {"_id.type":"https://schema.org/Book","attrs.https://schema=org/value.value":available},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listBook = []
    for res in resultbooks:
        book = []
        book.append(res.get("attrs").get("https://schema=org/isbn").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/title").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/description").get("value"))
        book.append(res.get("attrs").get("https://schema=org/author").get("value"))
        book.append(res.get("attrs").get("https://uri=fiware=org/ns/data-models#category").get("value"))
        book.append(res.get("attrs").get("https://schema=org/image").get("value"))
        book.append(res.get("attrs").get("https://schema=org/value").get("value"))
        listBook.append(book)
    return listBook

def list_all_books_filtered_by_isbn(entitiesCollection,isbn):
    resultbooks = entitiesCollection.find( {"_id.type":"https://schema.org/Book","attrs.https://schema=org/isbn.value":isbn},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listBook = []
    for res in resultbooks:
        book = []
        book.append(res.get("attrs").get("https://schema=org/isbn").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/title").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/description").get("value"))
        book.append(res.get("attrs").get("https://schema=org/author").get("value"))
        book.append(res.get("attrs").get("https://uri=fiware=org/ns/data-models#category").get("value"))
        book.append(res.get("attrs").get("https://schema=org/image").get("value"))
        book.append(res.get("attrs").get("https://schema=org/value").get("value"))
        listBook.append(book)
    return listBook

def list_all_books_filtered_by_autor(entitiesCollection,autor):
    resultbooks = entitiesCollection.find( {"_id.type":"https://schema.org/Book","attrs.https://schema=org/author.value":autor},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listBook = []
    for res in resultbooks:
        book = []
        book.append(res.get("attrs").get("https://schema=org/isbn").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/title").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/description").get("value"))
        book.append(res.get("attrs").get("https://schema=org/author").get("value"))
        book.append(res.get("attrs").get("https://uri=fiware=org/ns/data-models#category").get("value"))
        book.append(res.get("attrs").get("https://schema=org/image").get("value"))
        book.append(res.get("attrs").get("https://schema=org/value").get("value"))
        listBook.append(book)
    return listBook

def list_all_books_filtered_by_title(entitiesCollection,title):
    resultbooks = entitiesCollection.find( {"_id.type":"https://schema.org/Book","attrs.https://uri=etsi=org/ngsi-ld/title.value":title},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listBook = []
    for res in resultbooks:
        book = []
        book.append(res.get("attrs").get("https://schema=org/isbn").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/title").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/description").get("value"))
        book.append(res.get("attrs").get("https://schema=org/author").get("value"))
        book.append(res.get("attrs").get("https://uri=fiware=org/ns/data-models#category").get("value"))
        book.append(res.get("attrs").get("https://schema=org/image").get("value"))
        book.append(res.get("attrs").get("https://schema=org/value").get("value"))
        listBook.append(book)
    return listBook

def list_all_books_filtered_by_category(entitiesCollection,category):
    resultbooks = entitiesCollection.find( {"_id.type":"https://schema.org/Book","attrs.https://uri=fiware=org/ns/data-models#category.value":category},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listBook = []
    for res in resultbooks:
        book = []
        book.append(res.get("attrs").get("https://schema=org/isbn").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/title").get("value"))
        book.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/description").get("value"))
        book.append(res.get("attrs").get("https://schema=org/author").get("value"))
        book.append(res.get("attrs").get("https://uri=fiware=org/ns/data-models#category").get("value"))
        book.append(res.get("attrs").get("https://schema=org/image").get("value"))
        book.append(res.get("attrs").get("https://schema=org/value").get("value"))
        listBook.append(book)
    return listBook

def login(entitiesCollection,email,passw):
    passw = hashlib.md5(passw.encode('utf-8')).hexdigest()
    print(passw)
    resultPerson = entitiesCollection.find( {"_id.type":"https://schema.org/Person","attrs.https://schema=org/email.value":email,"attrs.https://schema=org/accessCode.value":passw},{"_id":1,"creDate":1, "attrs":1, "attrNames":1, "modDate":1, "lastCorrelator":1})
    listPerson = []
    listPersonInterest = []
    print(resultPerson)
    for res in resultPerson:
        person = []
        person.append(res.get("attrs").get("https://uri=etsi=org/ngsi-ld/name").get("value"))
        person.append(res.get("attrs").get("https://schema=org/familyName").get("value"))
        person.append(res.get("attrs").get("https://schema=org/memberOf").get("value"))
        listPersonInterest = res.get("attrs").get("https://schema=org/knowsAbout").get("value")
        listPerson.append(person)
    return listPerson,listPersonInterest

def insert_new_person(entitiesCollection,email,passw,name,surname,faculty):
    passw = hashlib.md5(passw.encode('utf-8')).hexdigest()
    print(passw)
    user = {
            "_id": {
                "id": "urn:ngsi-ld:Person:person" + str(random.randint(0, 999)),
                "type": "https://schema.org/Person",
                "servicePath": "/"
            },
            "attrNames": [
                "https://schema.org/email",
                "https://schema.org/familyName",
                "https://uri.etsi.org/ngsi-ld/name",
                "https://schema.org/memberOf",
                "https://schema.org/knowsAbout"
            ],
            "attrs": {
                "https://schema=org/email": {
                "type": "Property",
                "creDate": 1673640180.3143768,
                "modDate": 1673640180.3143768,
                "value": email,
                "mdNames": []
                },
                "https://schema=org/accessCode": {
                "type": "Property",
                "creDate": 1673691385.7333272,
                "modDate": 1673691385.7333272,
                "value": passw,
                "mdNames": []
                },
                "https://schema=org/familyName": {
                "type": "Property",
                "creDate": 1673640180.3143768,
                "modDate": 1673640180.3143768,
                "value": surname,
                "mdNames": []
                },
                "https://uri=etsi=org/ngsi-ld/name": {
                "type": "Property",
                "creDate": 1673640180.3143768,
                "modDate": 1673640180.3143768,
                "value": name,
                "mdNames": []
                },
                "https://schema=org/memberOf": {
                "type": "Property",
                "creDate": 1673640180.3143768,
                "modDate": 1673640180.3143768,
                "value": faculty,
                "mdNames": []
                },
                "https://schema=org/knowsAbout": {
                "type": "Property",
                "creDate": 1673640180.3143768,
                "modDate": 1673640180.3143768,
                "value": [faculty],
                "mdNames": []
                }
            },
            "creDate": 1673640180.3143768,
            "modDate": 1673640180.3143768,
            "lastCorrelator": ""
            }
    entitiesCollection.insert_one(user)

def insert_new_book(entitiesCollection,isbn,title,description,autor,category):
    book = {
            "_id": {
                "id": "urn:ngsi-ld:Book:book" + str(random.randint(0, 999)),
                "type": "https://schema.org/Book",
                "servicePath": "/"
            },
            "attrNames": [
                "https://schema.org/isbn",
                "https://uri.etsi.org/ngsi-ld/title",
                "https://uri.etsi.org/ngsi-ld/description",
                "https://schema.org/author",
                "https://uri.fiware.org/ns/data-models#category",
                "https://schema.org/image",
                "https://schema.org/value"
            ],
            "attrs": {
                "https://schema=org/isbn": {
                "type": "Property",
                "creDate": 1673639618.0196044,
                "modDate": 1673639618.0196044,
                "value": isbn,
                "mdNames": []
                },
                "https://uri=etsi=org/ngsi-ld/title": {
                "type": "Property",
                "creDate": 1673639618.0196044,
                "modDate": 1673639618.0196044,
                "value": title,
                "mdNames": []
                },
                "https://uri=etsi=org/ngsi-ld/description": {
                "type": "Property",
                "creDate": 1673639618.0196044,
                "modDate": 1673639618.0196044,
                "value": description,
                "mdNames": []
                },
                "https://schema=org/author": {
                "type": "Property",
                "creDate": 1673639618.0196044,
                "modDate": 1673639618.0196044,
                "value": autor,
                "mdNames": []
                },
                "https://uri=fiware=org/ns/data-models#category": {
                "type": "Property",
                "creDate": 1673639618.0196044,
                "modDate": 1673639618.0196044,
                "value": category,
                "mdNames": []
                },
                "https://schema=org/image": {
                "type": "Property",
                "creDate": 1673639618.0196044,
                "modDate": 1673639618.0196044,
                "value": "static/standardbook.jpeg",
                "mdNames": []
                },
                "https://schema=org/value": {
                "type": "Property",
                "creDate": 1673639618.0196044,
                "modDate": 1673639618.0196044,
                "value": "0",
                "mdNames": []
                }
            },
            "creDate": 1673639618.0196044,
            "modDate": 1673639618.0196044,
            "lastCorrelator": ""
            }
    entitiesCollection.insert_one(book)

def remove_book_by_isbn(entitiesCollection,isbn):
    entitiesCollection.delete_one({"attrs.https://schema=org/isbn.value":isbn})

def insert_new_category(entitiesCollection,categoryName):
    cat = {
            "_id": {
                "id": "urn:ngsi-ld:Category:category" + str(random.randint(0, 999)),
                "type": "https://schema.org/Category",
                "servicePath": "/"
            },
            "attrNames": [
                "https://uri.etsi.org/ngsi-ld/default-context/categoryName"
            ],
            "attrs": {
                "https://schema=org/name": {
                "type": "Property",
                "creDate": 1673635663.5077872,
                "modDate": 1673635663.5077872,
                "value": categoryName,
                "mdNames": []
                }
            },
            "creDate": 1673635663.5077872,
            "modDate": 1673635663.5077872,
            "lastCorrelator": ""
        }
    entitiesCollection.insert_one(cat)

def remove_category_by_name(entitiesCollection,categoryName):
    entitiesCollection.delete_one({"attrs.https://schema=org/name.value":categoryName})