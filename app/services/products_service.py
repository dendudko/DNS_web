from app.services.base_imports import *
from app.entities.models import Product
from app.dto.products_dto import SProduct, SProductUpdate


async def create_product(db: AsyncSession, product_data: SProduct) -> None:
    db.add(Product(id=product_data.product_id, name=product_data.name, price=product_data.price))
    await db.commit()


async def get_products(db: AsyncSession) -> List[SProduct]:
    products_query = await db.execute(select(Product))
    products = products_query.scalars().all()
    return [SProduct(product_id=product.id, name=product.name, price=product.price) for product in products]


async def update_product(db: AsyncSession, product_data: SProductUpdate) -> None:
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
