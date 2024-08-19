from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/promotions/", response_model=schemas.Promotion)
def create_promotion(promotion: schemas.PromotionCreate, db: Session = Depends(get_db)):
    return crud.create_promotion(db=db, promotion=promotion)

@router.get("/promotions/", response_model=List[schemas.Promotion])
def read_promotions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    promotions = crud.get_promotions(db, skip=skip, limit=limit)
    return promotions

@router.get("/promotions/{promotion_id}", response_model=schemas.Promotion)
def read_promotion(promotion_id: int, db: Session = Depends(get_db)):
    db_promotion = crud.get_promotion(db, promotion_id=promotion_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return db_promotion

@router.put("/promotions/{promotion_id}", response_model=schemas.Promotion)
def update_promotion(promotion_id: int, promotion: schemas.PromotionCreate, db: Session = Depends(get_db)):
    db_promotion = crud.get_promotion(db, promotion_id=promotion_id)
    if db_promotion is None:
        raise HTTPException(status_code=404, detail="Promotion not found")
    updated_promotion = crud.update_promotion(db=db, promotion=promotion, promotion_id=promotion_id)
    return updated_promotion
