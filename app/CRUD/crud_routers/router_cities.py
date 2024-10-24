from app.CRUD.crud_routers.router_base_imports import *
from app.CRUD.crud_models import crud_cities
from app.CRUD.crud_validation.validation_cities import CityResponse

router = APIRouter()


@router.post("/cities")
async def create_city_endpoint(city_data: CityResponse, db: AsyncSession = Depends(get_db)):
    await crud_cities.create_city(db, city_data)
    return {"message": "Город успешно создан"}


@router.get("/cities", response_model=List[CityResponse])
async def get_cities_endpoint(db: AsyncSession = Depends(get_db)):
    return await crud_cities.get_cities(db)


@router.put("/cities")
async def update_city_endpoint(city_data: CityResponse, db: AsyncSession = Depends(get_db)):
    await crud_cities.update_city(db, city_data)
    return {"message": "Город успешно обновлен"}


@router.delete("/cities/{city_id}")
async def delete_city_endpoint(city_id: int, db: AsyncSession = Depends(get_db)):
    await crud_cities.delete_city(db, city_id)
    return {"message": "Город успешно удален"}
