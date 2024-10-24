from pydantic import BaseModel


class StoreCreate(BaseModel):
    store_id: int
    name: str
    city_id: int


class StoreResponse(BaseModel):
    store_id: int
    name: str
    city: str


class StoreUpdate(BaseModel):
    store_id: int
    name: str = None
    city_id: int = None
