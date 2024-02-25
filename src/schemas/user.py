from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class UserInDB(UserBase):
    hashed_password: str


class UserInput(UserBase):
    password: str
