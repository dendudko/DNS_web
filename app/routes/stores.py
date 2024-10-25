from app.routes.base_imports import *
from app.services import stores_service
from app.dto.stores_dto import SStoreResponse, SStoreUpdate, SStoreCreate

router = APIRouter()


@router.post("/stores")
async def create_store_endpoint(store_data: SStoreCreate, db: AsyncSession = Depends(get_db)):
    await stores_service.create_store(db, store_data)
    return {"message": "Магазин успешно создан"}


@router.get("/stores", response_model=List[SStoreResponse])
async def get_stores_endpoint(db: AsyncSession = Depends(get_db)):
    return await stores_service.get_stores(db)


@router.put("/stores")
async def update_store_endpoint(store_data: SStoreUpdate, db: AsyncSession = Depends(get_db)):
    await stores_service.update_store(db, store_data)
    return {"message": "Магазин успешно обновлен"}


@router.delete("/stores/{store_id}")
async def delete_store_endpoint(store_id: int, db: AsyncSession = Depends(get_db)):
    await stores_service.delete_store(db, store_id)
    return {"message": "Магазин успешно удален"}
