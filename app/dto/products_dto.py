from pydantic import BaseModel


class SProduct(BaseModel):
    product_id: int
    name: str
    price: float


class SProductUpdate(BaseModel):
    product_id: int
    name: str = None
    price: float = None
