from sqlalchemy.orm import Session
from . import models, schemas

# Create coupon
def create_coupon(db: Session, coupon: schemas.CouponCreate):
    db_coupon = models.Coupon(**coupon.dict())
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon

# Get all coupons
def get_coupons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Coupon).offset(skip).limit(limit).all()

# Get a single coupon by ID
def get_coupon(db: Session, coupon_id: int):
    return db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()

def update_coupon(db: Session, coupon: schemas.CouponCreate, coupon_id: int):
    db_coupon = db.query(models.Coupon).filter(models.Coupon.id == coupon_id).first()
    if db_coupon is None:
        return None
    for var, value in vars(coupon).items():
        setattr(db_coupon, var, value) if value else None
    db.commit()
    db.refresh(db_coupon)
    return db_coupon


# Create promotion
def create_promotion(db: Session, promotion: schemas.PromotionCreate):
    db_promotion = models.Promotion(**promotion.dict())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

# Get all promotions
def get_promotions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Promotion).offset(skip).limit(limit).all()

# Get a single promotion by ID
def get_promotion(db: Session, promotion_id: int):
    return db.query(models.Promotion).filter(models.Promotion.id == promotion_id).first()

# Update promotion
def update_promotion(db: Session, promotion: schemas.PromotionCreate, promotion_id: int):
    db_promotion = db.query(models.Promotion).filter(models.Promotion.id == promotion_id).first()
    if db_promotion is None:
        return None
    for var, value in vars(promotion).items():
        setattr(db_promotion, var, value) if value else None
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

# Delete promotion
def delete_promotion(db: Session, promotion_id: int):
    db_promotion = db.query(models.Promotion).filter(models.Promotion.id == promotion_id).first()
    if db_promotion is not None:
        db.delete(db_promotion)
        db.commit()
    return db_promotion
