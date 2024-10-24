from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    name = Column(String, unique=True, index=True)

    stores = relationship("Store", back_populates="city")


class Store(Base):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    name = Column(String, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))

    city = relationship("City", back_populates="stores")
    sales = relationship("Sale", back_populates="store")


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    name = Column(String, index=True)
    price = Column(Float)


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    store_id = Column(Integer, ForeignKey('stores.id'))
    sale_datetime = Column(DateTime, server_default=func.now())

    store = relationship("Store", back_populates="sales")
    items = relationship("SaleItem", back_populates="sale")


class SaleItem(Base):
    __tablename__ = 'sale_items'
    sale_id = Column(Integer, ForeignKey('sales.id'), primary_key=True, autoincrement=False)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    count = Column(Integer, nullable=False)

    sale = relationship("Sale", back_populates="items")
    product = relationship("Product")
