from fastapi import APIRouter, Request
from typing import List
from fastapi.responses import JSONResponse
from services.bookService import get_all_books

router = APIRouter()


@router.get("/")
async def get_books(req: Request):
    books = await get_all_books(req.app.db["db"])
    print(books)
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "message": "Found books",
            "data": {"books": books},
            "errors": [],
        },
    )


@router.get("/{id}")
async def get_book_by_id(req: Request, id: str):
    return {"username": "fakecurrentuser"}


@router.delete("/{id}")
async def delete_book_by_id(username: str):
    return {"username": username}


@router.post("/")
async def create_book(username: str):
    return {"username": username}


@router.patch("/{id}")
async def update_book_by_id(username: str):
    return {"username": username}
