from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy import func
from datetime import datetime, timedelta
from typing import List
from app.entities.models import Sale, Store, City, Product, SaleItem
from app.dto.validation_methods import MethodsRequest
from app.dto.validation_sales import SaleResponse, ProductResponseExt, StoreResponse


async def get_sales_combined(db: AsyncSession, methods: MethodsRequest) -> List[SaleResponse]:
    query = (select(Sale).
             options(selectinload(Sale.store).selectinload(Store.city),
                     selectinload(Sale.items).selectinload(SaleItem.product))
             .join(Sale.items).join(Product).join(Store).join(City))

    total_amount = func.sum(SaleItem.count * Product.price).label('total_amount')
    query = query.add_columns(total_amount).group_by(Sale.id, Store.id, City.id)

    if methods.city_id:
        query = query.where(methods.city_id == City.id)
    if methods.store_id:
        query = query.where(methods.store_id == Store.id)
    if methods.product_id:
        query = query.where(methods.product_id == Product.id)
    if methods.last_days:
        date_threshold = datetime.now() - timedelta(days=methods.last_days)
        query = query.where(Sale.sale_datetime >= date_threshold)
    if methods.amount:
        if methods.amount_comparison == "more":
            query = query.having(total_amount > methods.amount)
        else:
            query = query.having(total_amount < methods.amount)
    if methods.quantity:
        if methods.quantity_comparison == "more":
            query = query.having(func.sum(SaleItem.count) > methods.quantity)
        else:
            query = query.having(func.sum(SaleItem.count) < methods.quantity)
    if methods.sale_id:
        query = query.where(methods.sale_id == Sale.id)

    sales_query = await db.execute(query)
    sales = sales_query.all()

    sales_with_items = []
    for sale_row in sales:
        sale = sale_row.Sale
        total_price = sale_row.total_amount
        store = sale.store
        sale_items_response = []

        for item in sale.items:
            product = item.product
            total_product_price = product.price * item.count

            sale_items_response.append(ProductResponseExt(
                product_id=product.id,
                name=product.name,
                price=product.price,
                count=item.count,
                total_product_price=total_product_price
            ))

        sale_response = SaleResponse(
            sale_id=sale.id,
            store=StoreResponse(
                store_id=store.id,
                name=store.name,
                city=store.city.name
            ),
            items=sale_items_response,
            total_price=total_price,
            sale_datetime=sale.sale_datetime
        )
        sales_with_items.append(sale_response)

    return sales_with_items
