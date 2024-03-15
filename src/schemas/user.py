from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


fake_users_db = {
    "admin": {
        "username": "admin",
        "full_name": "super admin",
        "email": "admin@example.com",
        "hashed_password": "$2b$12$AESsQc/6lKloIjRwmswtneckeAFwH4Z7NOBi7777R9wmzTTH1coo6",
        "disabled": False,
    }
}


def get_user(db, username: str) -> UserInDB | None:
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
