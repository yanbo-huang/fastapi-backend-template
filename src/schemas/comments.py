from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class Comment(BaseModel):
    creation_time: datetime
    last_modified_time: datetime
    content: str = Field(max_length=500)

    model_config = ConfigDict(from_attributes=True)
