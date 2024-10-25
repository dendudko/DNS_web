from pydantic import BaseModel


class SMethodsRequest(BaseModel):
    city_id: int = None
    store_id: int = None
    product_id: int = None
    last_days: int = None
    amount: float = None
    amount_comparison: str = "more"
    quantity: int = None
    quantity_comparison: str = "more"
    sale_id: int = None
