from app.routes.base_imports import *
from app.services import sales_service
from app.dto.sales_dto import SSaleCreate, SSaleResponse

router = APIRouter()


@router.post("/sales")
async def create_sale_endpoint(sale_data: SSaleCreate, db: AsyncSession = Depends(get_db)):
    await sales_service.create_sale(db, sale_data)
    return {"message": "Продажа успешно создана"}


@router.get("/sales", response_model=List[SSaleResponse])
async def get_sales_endpoint(db: AsyncSession = Depends(get_db)):
    return await sales_service.get_sales(db)


@router.put("/sales")
async def update_sale_endpoint(sale_data: SSaleCreate, db: AsyncSession = Depends(get_db)):
    await sales_service.update_sale(db, sale_data)
    return {"message": "Продажа успешно обновлена"}


@router.delete("/sales/{sale_id}")
async def delete_sale_endpoint(sale_id: int, db: AsyncSession = Depends(get_db)):
    await sales_service.delete_sale(db, sale_id)
    return {"message": "Продажа успешно удалена"}
