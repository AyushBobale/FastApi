from database.db import conn

# last resort connect directly from here
from models.bookModel import Book


async def get_all_books(db):
    books = []
    cur = db.books.find({})
    async for doc in cur:
        books.append(Book(**doc))
    return books


async def create_book(db, book):
    doc = book
    res = await db.books.insert_one(doc)
    return doc


async def update_book(db, id, book):
    pass
