from app.services.base_imports import *
from app.entities.models import Store
from app.dto.validation_stores import StoreResponse, StoreUpdate, StoreCreate


async def create_store(db: AsyncSession, store_data: StoreCreate) -> None:
    db.add(Store(id=store_data.store_id, name=store_data.name, city_id=store_data.city_id))
    await db.commit()


async def get_stores(db: AsyncSession) -> List[StoreResponse]:
    stores_query = await db.execute(select(Store).options(selectinload(Store.city)))
    stores = stores_query.scalars().all()
    return [StoreResponse(store_id=store.id, name=store.name, city=store.city.name)
            for store in stores]


async def update_store(db: AsyncSession, store_data: StoreUpdate) -> None:
    store_query = await db.execute(select(Store).where(store_data.store_id == Store.id))
    store = store_query.scalar_one_or_none()
    if not store:
        raise HTTPException(status_code=404, detail="Магазин не найден")
    if store_data.name and store_data.name != store.name:
        store.name = store_data.name
    if store_data.city_id and store_data.city_id != store.city_id:
        store.city_id = store_data.city_id
    await db.commit()


async def delete_store(db: AsyncSession, store_id: int) -> None:
    store_query = await db.execute(select(Store).where(store_id == Store.id))
    store = store_query.scalar_one_or_none()
    if not store:
        raise HTTPException(status_code=404, detail="Магазин не найден")
    await db.execute(delete(Store).where(store.id == Store.id))
    await db.commit()
