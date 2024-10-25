from app.routes.base_imports import *
from app.services import cities_service
from app.dto.cities_dto import SCity

router = APIRouter()


@router.post("/cities")
async def create_city_endpoint(city_data: SCity, db: AsyncSession = Depends(get_db)):
    await cities_service.create_city(db, city_data)
    return {"message": "Город успешно создан"}


@router.get("/cities", response_model=List[SCity])
async def get_cities_endpoint(db: AsyncSession = Depends(get_db)):
    return await cities_service.get_cities(db)


@router.put("/cities")
async def update_city_endpoint(city_data: SCity, db: AsyncSession = Depends(get_db)):
    await cities_service.update_city(db, city_data)
    return {"message": "Город успешно обновлен"}


@router.delete("/cities/{city_id}")
async def delete_city_endpoint(city_id: int, db: AsyncSession = Depends(get_db)):
    await cities_service.delete_city(db, city_id)
    return {"message": "Город успешно удален"}
