from typing import Union

from fastapi import FastAPI
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from pymongo import MongoClient
from routers import booksRouter

config = dotenv_values(".env")
app = FastAPI()
app.include_router(booksRouter.router)


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["DB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


@app.get("/")
def root():
    return {
        "sucess": True,
        "message": "Server running !",
        "errors": [],
        "data": {}
    }


@app.get("/items/{item_id}")
def read_item(request: Request, item_id: int, q: str | None = None):

    # docs = conn.analystai.test.find({})
    # print([doc for doc in docs])
    docs = request.app.database.test.find({})
    print([doc for doc in docs])
    return {"item_id": item_id, "q": q}
