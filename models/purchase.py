from sqlalchemy import  Column, Integer, Float, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base
class Purchase(Base):
    __tablename__ = 'purchases'
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    amount = Column(Float)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))



