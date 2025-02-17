from sqlalchemy import Column, Integer, String
from api.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    userId = Column(Integer, autoincrement=True)
