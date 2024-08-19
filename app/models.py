from sqlalchemy import Column, Integer, String, Float, Date #, ForeignKey
# from sqlalchemy.orm import relationship
from .database import Base

class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    discount = Column(Float)
    initialDate = Column(Date)
    finalDate = Column(Date)
    
    # Test relationship.
    # promotion_id = Column(Integer, ForeignKey("promotions.id"))
    # promotion = relationship("Promotion", back_populates="coupons")

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    initialDate = Column(Date)
    finalDate = Column(Date)
    discount = Column(Float)

    # Test relationship
    # coupons = relationship("Coupon", back_populates="promotion")
