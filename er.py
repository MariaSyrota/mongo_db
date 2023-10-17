from pymongo import database
import pymongo
import certifi
from confing import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}@cluster0.jhmpvi4.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(url, tlsCAFile=certifi.where())
fantasy_books = database.books
school_books = database.school_books

fantasy_books.insert_one({
    "title": "Гра престолів",
    "price": 200,
    "year": 1996,
    "pages": 800,
})
school_books.insert_many([
    {
        "title": "Історія України",
        "class": 10,
        "pages": 200,
        "year":2012,
    },
    {
        "title": "Алгебра",
        "class": 9,
        "pages": 150,
        "year":2021,
    },
    {
        "title": "Біологія",
        "class": 11,
        "pages": 180,
        "year":2023,
    },
    {
        "title": "Географія",
        "class": 8,
        "pages": 160,
        "year":1999,
    },
    {
        "title": "Англійська мова",
        "class": 7,
        "pages": 120,
        "year":2009,
    }
])
fantasy_books.update_one({"title": "Гра престолів"}, {"$inc": {"price": 56}})
history_book = school_books.find_one({"title": {"$regex": "історія", "$options": "i"}})
print(history_book)
fantasy_books.delete_one({"title": "Гра престолів"})
school_books.delete_many({"year": {"$lt": 2020}})
