from app.services.base_imports import *
from app.entities.models import Sale, Store, Product, SaleItem
from app.dto.validation_sales import (SaleCreate, SaleResponse,
                                      ProductResponseExt, StoreResponse)


async def create_sale_items(db: AsyncSession, sale_data: SaleCreate):
    for item_data in sale_data.items:
        product_query = await db.execute(select(Product).where(item_data.product_id == Product.id))
        product = product_query.scalar_one_or_none()
        if not product:
            raise HTTPException(status_code=404, detail=f"Товар с id={item_data.product_id} не найден")
        sale_item = SaleItem(
            sale_id=sale_data.sale_id,
            product_id=product.id,
            count=item_data.count
        )
        db.add(sale_item)


async def create_sale(db: AsyncSession, sale_data: SaleCreate) -> None:
    store_query = await db.execute(select(Store).where(sale_data.store_id == Store.id))
    store = store_query.scalar_one_or_none()
    if not store:
        raise HTTPException(status_code=404, detail="Магазин не найден")
    new_sale = Sale(id=sale_data.sale_id, store_id=sale_data.store_id)
    db.add(new_sale)
    await db.flush()
    await create_sale_items(db, sale_data)
    await db.commit()


async def get_sales(db: AsyncSession) -> List[SaleResponse]:
    sales_query = await db.execute(
        select(Sale)
        .options(selectinload(Sale.items))
        .options(selectinload(Sale.store).selectinload(Store.city))
    )
    sales = sales_query.scalars().all()
    sales_with_items = []

    for sale in sales:
        store = sale.store
        sale_items_response = []
        total_price = 0

        for item in sale.items:
            product_query = await db.execute(select(Product).where(item.product_id == Product.id))
            product = product_query.scalar_one()
            total_product_price = product.price * item.count
            sale_items_response.append(ProductResponseExt(
                product_id=product.id,
                name=product.name,
                price=product.price,
                count=item.count,
                total_product_price=total_product_price
            ),
            )
            total_price += total_product_price

        sale_response = SaleResponse(
            sale_id=sale.id,
            store=StoreResponse(
                store_id=store.id,
                name=store.name,
                city=store.city.name
            ),
            items=sale_items_response,
            total_price=total_price
        )
        sales_with_items.append(sale_response)

    return sales_with_items


async def update_sale(db: AsyncSession, sale_data: SaleCreate) -> None:
    sale_query = await db.execute(select(Sale).where(sale_data.sale_id == Sale.id))
    sale = sale_query.scalar_one_or_none()
    if not sale:
        raise HTTPException(status_code=404, detail="Продажа не найдена")

    if sale_data.store_id and sale.store_id != sale_data.store_id:
        store_query = await db.execute(select(Store).where(sale_data.store_id == Store.id))
        store = store_query.scalar_one_or_none()
        if not store:
            raise HTTPException(status_code=404, detail="Магазин не найден")
        sale.store_id = sale_data.store_id

    await db.execute(delete(SaleItem).where(sale.id == SaleItem.sale_id))
    await create_sale_items(db, sale_data)
    await db.commit()


async def delete_sale(db: AsyncSession, sale_id: int) -> None:
    sale_query = await db.execute(select(Sale).where(sale_id == Sale.id))
    sale = sale_query.scalar_one_or_none()
    if not sale:
        raise HTTPException(status_code=404, detail="Продажа не найдена")
    await db.execute(delete(SaleItem).where(sale.id == SaleItem.sale_id))
    await db.execute(delete(Sale).where(sale.id == Sale.id))
    await db.commit()
