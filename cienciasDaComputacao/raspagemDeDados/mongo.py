from pymongo import MongoClient

client = MongoClient()

db = client.catalogue

book = {"title": "A Light in the Attic"}

db.books.insert_one(book)

students = db.books

client.close()
