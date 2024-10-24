from app.CRUD.crud_validation.validation_base_imports import *


class CityResponse(BaseModel):
    city_id: int
    name: str
