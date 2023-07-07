from pydantic import BaseModel
from typing import Optional, List
from bson.objectid import ObjectId
from pydantic import Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class CustomerRating(BaseModel):
    rating: int
    customer_id: Optional[str]


class Book(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    author: str
    description: str
    cover_image: str
    price: float
    customer_rating: Optional[List[CustomerRating]] = []
