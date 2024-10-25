from pydantic import BaseModel


class SStoreCreate(BaseModel):
    store_id: int
    name: str
    city_id: int


class SStoreResponse(BaseModel):
    store_id: int
    name: str
    city: str


class SStoreUpdate(BaseModel):
    store_id: int
    name: str = None
    city_id: int = None
