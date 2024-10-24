from pydantic import BaseModel
from typing import List
from datetime import datetime


class ProductResponse(BaseModel):
    product_id: int
    name: str
    price: float
    count: int
    total_product_price: float


class StoreResponse(BaseModel):
    store_id: int
    name: str
    city: str


class SaleResponse(BaseModel):
    sale_id: int
    store: StoreResponse
    items: List[ProductResponse]
    total_price: float
    sale_datetime: datetime = None


class SaleItemCreate(BaseModel):
    product_id: int
    count: int


class SaleCreate(BaseModel):
    sale_id: int
    store_id: int
    items: List[SaleItemCreate]
