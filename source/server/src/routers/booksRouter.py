import json
from fastapi import APIRouter, Request
from typing import List
from fastapi.responses import JSONResponse
from services.bookService import get_all_books_serv, create_book_serv
from models.bookModel import Book

router = APIRouter()


@router.get("/")
async def get_books(req: Request):
    books = await get_all_books_serv(req.app.db["db"])

    if books:
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Found books",
                "data": {"books": books},
                "errors": [],
            },
        )

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": "Could not fetch books",
            "data": {},
            "errors": [],
        },
    )


@router.post("/")
async def create_book(req: Request, book: Book):
    res_book = await create_book_serv(req.app.db["db"], book.dict())
    if res_book:
        return JSONResponse(
            status_code=200,
            content={
                "success": True,
                "message": "Book created",
                "data": {"book": res_book},
                "errors": [],
            },
        )

    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": "Book not created",
            "data": {},
            "errors": [],
        },
    )


@router.get("/{id}")
async def get_book_by_id(req: Request, id: str):
    return {"username": "fakecurrentuser"}


@router.delete("/{id}")
async def delete_book_by_id(username: str):
    return {"username": username}


@router.patch("/{id}")
async def update_book_by_id(username: str):
    return {"username": username}
