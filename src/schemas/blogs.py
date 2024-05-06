from pydantic import BaseModel, ConfigDict, Field

from src.schemas.user import UserBase


class BlogCreate(BaseModel):
    title: str = Field(max_length=55)
    content: str = Field(max_length=280)


class BlogDTO(BlogCreate):
    owner: UserBase

    model_config = ConfigDict(from_attributes=True)


class BlogInDB(BlogCreate):
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
