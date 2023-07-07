from utils.util import ObjIDParser
from models.bookModel import Book


async def get_all_books_serv(db):
    books = []
    cur = db.books.find({})
    async for doc in cur:
        books.append(ObjIDParser(Book(**doc)))
    return books


async def create_book_serv(db, book):
    doc = book
    res = await db.books.insert_one(doc)
    print(res)
    return ObjIDParser(Book(**doc))


async def update_book(db, id, book):
    pass
