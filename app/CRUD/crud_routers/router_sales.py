from app.CRUD.crud_routers.router_base_imports import *
from app.CRUD.crud_models import crud_sales
from app.CRUD.crud_validation.validation_sales import SaleCreate, SaleResponse

router = APIRouter()


@router.post("/sales")
async def create_sale_endpoint(sale_data: SaleCreate, db: AsyncSession = Depends(get_db)):
    await crud_sales.create_sale(db, sale_data)
    return {"message": "Продажа успешно создана"}


@router.get("/sales", response_model=List[SaleResponse])
async def get_sales_endpoint(db: AsyncSession = Depends(get_db)):
    return await crud_sales.get_sales(db)


@router.put("/sales")
async def update_sale_endpoint(sale_data: SaleCreate, db: AsyncSession = Depends(get_db)):
    await crud_sales.update_sale(db, sale_data)
    return {"message": "Продажа успешно обновлена"}


@router.delete("/sales/{sale_id}")
async def delete_sale_endpoint(sale_id: int, db: AsyncSession = Depends(get_db)):
    await crud_sales.delete_sale(db, sale_id)
    return {"message": "Продажа успешно удалена"}
