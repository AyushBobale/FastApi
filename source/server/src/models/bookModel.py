from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID, uuid4


class CustomerRating(BaseModel):
    rating: int
    customer_id: Optional[str]


class Book(BaseModel):
    _id: Optional[str] = str(uuid4())
    title: str
    author: str
    description: str
    cover_image: str
    price: float
    customer_rating: Optional[List[CustomerRating]] = []
