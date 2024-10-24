from app.services.base_imports import *
from app.entities.models import City
from app.dto.validation_cities import List, CityResponse


async def create_city(db: AsyncSession, city_data: CityResponse) -> None:
    db.add(City(id=city_data.city_id, name=city_data.name))
    await db.commit()


async def get_cities(db: AsyncSession) -> List[CityResponse]:
    cities_query = await db.execute(select(City))
    cities = cities_query.scalars().all()
    return [CityResponse(city_id=city.id, name=city.name) for city in cities]


async def update_city(db: AsyncSession, city_data: CityResponse) -> None:
    city_query = await db.execute(select(City).where(city_data.city_id == City.id))
    city = city_query.scalar_one_or_none()
    if not city:
        raise HTTPException(status_code=404, detail="Город не найден")
    if city_data.name != city.name:
        city.name = city_data.name
    await db.commit()


async def delete_city(db: AsyncSession, city_id: int) -> None:
    city_query = await db.execute(select(City).where(city_id == City.id))
    city = city_query.scalar_one_or_none()
    if not city:
        raise HTTPException(status_code=404, detail="Город не найден")
    await db.execute(delete(City).where(city.id == City.id))
    await db.commit()
