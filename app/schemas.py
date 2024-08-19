from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class CouponBase(BaseModel):
    code: str
    discount: float
    initialDate: date
    finalDate: date

class CouponCreate(CouponBase):
    pass

class Coupon(CouponBase):
    id: int
    # promotion_id: Optional[int]

    class Config:
        orm_mode = True

class PromotionBase(BaseModel):
    description: str
    initialDate: date
    finalDate: date
    discount: float

class PromotionCreate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int
    coupons: List[Coupon] = []

    class Config:
        orm_mode = True
