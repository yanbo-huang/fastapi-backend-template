from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.database.dependencies import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String(55))
    content = Column(String(280))

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="blogs")
