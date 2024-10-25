from pydantic import BaseModel


class SCity(BaseModel):
    city_id: int
    name: str
