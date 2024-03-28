
from fastapi import APIRouter, Depends
from sqlalchemy import select

from src.database import DBSession
from src.models.users import User
from src.schemas.token import TokenData
from src.schemas.user import UserInput, UserBase
from src.security import get_password_hash, validate_token

router = APIRouter()


@router.post("/", response_model=UserBase)
async def create_user(
        user_in: UserInput,
        db_session: DBSession,
) -> UserBase:
    hashed_password = get_password_hash(user_in.password)
    user_create = User(username=user_in.username, email=user_in.email, hashed_password=hashed_password)
    db_session.add(user_create)
    db_session.commit()

    return UserBase.model_validate(user_create)


@router.get("/", response_model=list[UserBase], dependencies=[Depends(validate_token)])
async def get_users(
        db_session: DBSession,
) -> list[UserBase]:
    all_users = db_session.execute(
        select(User)
    ).scalars().all()

    return [UserBase.model_validate(user) for user in all_users]
