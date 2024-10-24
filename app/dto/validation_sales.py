from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.dto.validation_stores import StoreResponse
from app.dto.validation_products import ProductResponse


class ProductResponseExt(ProductResponse):
    count: int
    total_product_price: float


class SaleResponse(BaseModel):
    sale_id: int
    store: StoreResponse
    items: List[ProductResponseExt]
    total_price: float
    sale_datetime: datetime = None


class SaleItemCreate(BaseModel):
    product_id: int
    count: int


class SaleCreate(BaseModel):
    sale_id: int
    store_id: int
    items: List[SaleItemCreate]
