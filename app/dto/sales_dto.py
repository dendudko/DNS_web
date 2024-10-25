from pydantic import BaseModel
from typing import List
from datetime import datetime
from app.dto.stores_dto import SStoreResponse
from app.dto.products_dto import SProduct


class SProductExt(SProduct):
    count: int
    total_product_price: float


class SSaleResponse(BaseModel):
    sale_id: int
    store: SStoreResponse
    items: List[SProductExt]
    total_price: float
    sale_datetime: datetime = None


class SSaleItemCreate(BaseModel):
    product_id: int
    count: int


class SSaleCreate(BaseModel):
    sale_id: int
    store_id: int
    items: List[SSaleItemCreate]
