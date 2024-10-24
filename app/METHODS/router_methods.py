from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database.db_connector import get_db
from app.METHODS import model_methods
from app.METHODS.validation_methods import MethodsRequest
from app.CRUD.crud_validation.validation_sales import SaleResponse

router = APIRouter()


@router.get("/sales/filter", response_model=List[SaleResponse])
async def get_sales(selected_methods: MethodsRequest, db: AsyncSession = Depends(get_db)):
    return await model_methods.get_sales_combined(db, selected_methods)
