from app.routes.base_imports import *
from app.services import methods_service
from app.dto.validation_methods import MethodsRequest
from app.dto.validation_sales import SaleResponse

router = APIRouter()


@router.get("/sales/filter", response_model=List[SaleResponse])
async def get_sales(selected_methods: MethodsRequest, db: AsyncSession = Depends(get_db)):
    return await methods_service.get_sales_combined(db, selected_methods)
