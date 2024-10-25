from app.routes.base_imports import *
from app.services import methods_service
from app.dto.methods_dto import SMethodsRequest
from app.dto.sales_dto import SSaleResponse

router = APIRouter()


@router.get("/sales/filter", response_model=List[SSaleResponse])
async def get_sales(selected_methods: SMethodsRequest, db: AsyncSession = Depends(get_db)):
    return await methods_service.get_sales_combined(db, selected_methods)
