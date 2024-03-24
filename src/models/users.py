from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))

    blogs = relationship("Blog", back_populates="owner")
