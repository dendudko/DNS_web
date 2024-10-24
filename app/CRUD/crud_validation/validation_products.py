from app.CRUD.crud_validation.validation_base_imports import *


class ProductResponse(BaseModel):
    product_id: int
    name: str
    price: float


class ProductUpdate(BaseModel):
    product_id: int
    name: str = None
    price: float = None
