from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import asyncio
from datetime import datetime
from app.entities.models import City, Store, Product, Sale, SaleItem
from app.database.db_connector import get_db


async def clear_tables(db: AsyncSession):
    await db.execute(text("DELETE FROM sale_items;"))
    for table in 'sales', 'stores', 'cities', 'products':
        await db.execute(text(f"DELETE FROM {table};"))
    await db.commit()


async def fill_tables(db: AsyncSession):
    cities = [
        City(id=1, name="Владивосток"),
        City(id=2, name="Артем"),
        City(id=3, name="Находка"),
    ]
    db.add_all(cities)
    await db.commit()

    stores = [
        Store(id=1, name="Бытовуха", city_id=1),
        Store(id=2, name="Быт или не быт", city_id=1),
        Store(id=3, name="Мастер на все руки", city_id=1),
        Store(id=4, name="Бытовуха", city_id=2),
        Store(id=5, name="Быт или не быт", city_id=2),
        Store(id=6, name="Сделай Сам", city_id=2),
        Store(id=7, name="Бытовуха", city_id=3),
        Store(id=8, name="Быт или не быт", city_id=3),
        Store(id=9, name="Домашний уют", city_id=3),
    ]
    db.add_all(stores)
    await db.commit()

    products = [
        Product(id=1, name="Пылесос", price=7500),
        Product(id=2, name="Стиральная машина", price=30000),
        Product(id=3, name="Холодильник", price=25000),
        Product(id=4, name="Микроволновая печь", price=8000),
        Product(id=5, name="Утюг", price=4000),
        Product(id=6, name="Электрочайник", price=2500),
        Product(id=7, name="Тостер", price=2000),
        Product(id=8, name="Кофемашина", price=12000),
        Product(id=9, name="Мясорубка", price=5000),
        Product(id=10, name="Электроплита", price=15000),
    ]
    # Маркетинг
    for p in products:
        p.price -= 10
    db.add_all(products)
    await db.commit()

    sales = [
        Sale(id=1, store_id=1),
        Sale(id=2, store_id=1, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=3, store_id=2, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=4, store_id=2, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=5, store_id=3, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=6, store_id=3, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=7, store_id=4, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=8, store_id=4, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=9, store_id=5, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=10, store_id=5, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=11, store_id=6, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=12, store_id=6, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=13, store_id=7, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=14, store_id=7, sale_datetime=datetime.strptime('2020-10-24 16:24:06.781630', '%Y-%m-%d %H:%M:%S.%f')),
        Sale(id=15, store_id=8),
        Sale(id=16, store_id=8),
        Sale(id=17, store_id=9),
        Sale(id=18, store_id=9),
    ]
    db.add_all(sales)
    await db.commit()

    sale_items = [
        SaleItem(sale_id=1, product_id=1, count=2),
        SaleItem(sale_id=1, product_id=2, count=1),
        SaleItem(sale_id=2, product_id=3, count=1),
        SaleItem(sale_id=2, product_id=4, count=3),
        SaleItem(sale_id=3, product_id=5, count=1),
        SaleItem(sale_id=3, product_id=6, count=2),
        SaleItem(sale_id=4, product_id=7, count=5),
        SaleItem(sale_id=4, product_id=8, count=1),
        SaleItem(sale_id=5, product_id=9, count=3),
        SaleItem(sale_id=5, product_id=10, count=1),
        SaleItem(sale_id=6, product_id=1, count=1),
        SaleItem(sale_id=6, product_id=2, count=2),
        SaleItem(sale_id=7, product_id=3, count=1),
        SaleItem(sale_id=7, product_id=4, count=1),
        SaleItem(sale_id=8, product_id=5, count=2),
        SaleItem(sale_id=8, product_id=6, count=1),
        SaleItem(sale_id=9, product_id=7, count=1),
        SaleItem(sale_id=9, product_id=8, count=1),
        SaleItem(sale_id=10, product_id=9, count=2),
        SaleItem(sale_id=10, product_id=10, count=1),
        SaleItem(sale_id=11, product_id=1, count=2),
        SaleItem(sale_id=11, product_id=2, count=1),
        SaleItem(sale_id=12, product_id=3, count=1),
        SaleItem(sale_id=12, product_id=4, count=3),
        SaleItem(sale_id=13, product_id=5, count=1),
        SaleItem(sale_id=13, product_id=6, count=2),
        SaleItem(sale_id=14, product_id=7, count=5),
        SaleItem(sale_id=14, product_id=8, count=1),
        SaleItem(sale_id=15, product_id=9, count=3),
        SaleItem(sale_id=15, product_id=10, count=1),
        SaleItem(sale_id=16, product_id=1, count=1),
        SaleItem(sale_id=16, product_id=2, count=2),
        SaleItem(sale_id=17, product_id=3, count=1),
        SaleItem(sale_id=17, product_id=4, count=1),
        SaleItem(sale_id=18, product_id=5, count=2),
        SaleItem(sale_id=18, product_id=6, count=1),
    ]
    db.add_all(sale_items)
    await db.commit()


async def main():
    async for session in get_db():
        await clear_tables(session)
        await fill_tables(session)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
