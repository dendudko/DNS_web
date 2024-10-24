from app.routes.base_imports import *
from app.services import products_service
from app.dto.validation_products import ProductResponse, ProductUpdate

router = APIRouter()


@router.post("/products")
async def create_product_endpoint(product_data: ProductResponse, db: AsyncSession = Depends(get_db)):
    await products_service.create_product(db, product_data)
    return {"message": "Товар успешно создан"}


@router.get("/products", response_model=List[ProductResponse])
async def get_products_endpoint(db: AsyncSession = Depends(get_db)):
    return await products_service.get_products(db)


@router.put("/products")
async def update_product_endpoint(product_data: ProductUpdate, db: AsyncSession = Depends(get_db)):
    await products_service.update_product(db, product_data)
    return {"message": "Товар успешно обновлен"}


@router.delete("/products/{product_id}")
async def delete_product_endpoint(product_id: int, db: AsyncSession = Depends(get_db)):
    await products_service.delete_product(db, product_id)
    return {"message": "Товар успешно удален"}
