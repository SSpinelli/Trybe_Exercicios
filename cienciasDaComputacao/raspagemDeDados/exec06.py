# Escreva um programa que se conecte ao banco de dados library
# e liste os livros da coleção books para uma
# determinada categoria recebida por uma pessoa usuária.
# Somente o título dos livros deve ser exibido.

from pymongo import MongoClient

client = MongoClient()

db = client.library

books = db.books

for book in books.find({}):
    print(book["title"])

client.close()
