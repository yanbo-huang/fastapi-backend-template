from pydantic import BaseModel, Field, ConfigDict

from src.models.users import User


class Blog(BaseModel):
    title: str = Field(max_length=55)
    content: str = Field(max_length=280)
    own: User

    model_config = ConfigDict(from_attributes=True)
