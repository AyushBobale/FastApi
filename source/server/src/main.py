from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import dotenv_values
from routers import booksRouter
from database.db import ping_server

config = dotenv_values(".env")
origins = [config["CORS_ORIGIN"]]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(booksRouter.router, prefix="/books")


@app.on_event("startup")
async def startup_db_client():
    app.db = await ping_server(config["DB_URI"])


@app.on_event("shutdown")
def shutdown_db_client():
    pass


@app.get("/")
def root():
    return JSONResponse(
        status_code=200,
        content={
            "sucess": True,
            "message": "Server running !",
            "errors": [],
            "data": {"db": []},
        },
    )
