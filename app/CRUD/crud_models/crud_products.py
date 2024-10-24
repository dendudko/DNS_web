from app.CRUD.crud_models.crud_base_imports import *
from app.database.models import Product
from app.CRUD.crud_validation.validation_products import List, ProductResponse, ProductUpdate


async def create_product(db: AsyncSession, product_data: ProductResponse) -> None:
    db.add(Product(id=product_data.product_id, name=product_data.name, price=product_data.price))
    await db.commit()


async def get_products(db: AsyncSession) -> List[ProductResponse]:
    products_query = await db.execute(select(Product))
    products = products_query.scalars().all()
    return [ProductResponse(product_id=product.id, name=product.name, price=product.price) for product in products]


async def update_product(db: AsyncSession, product_data: ProductUpdate) -> None:
    product_query = await db.execute(select(Product).where(product_data.product_id == Product.id))
    product = product_query.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    if product_data.name and product_data.name != product.name:
        product.name = product_data.name
    if product_data.price and product_data.price != product.price:
        product.price = product_data.price
    await db.commit()


async def delete_product(db: AsyncSession, product_id: int) -> None:
    product_query = await db.execute(select(Product).where(product_id == Product.id))
    product = product_query.scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Товар не найден")
    await db.execute(delete(Product).where(product.id == Product.id))
    await db.commit()
