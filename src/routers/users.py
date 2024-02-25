from fastapi import APIRouter, Depends
from sqlalchemy import select

from src import crud
from src.database.dependencies import DBSession
from src.database.models.users import User
from src.schemas.user import UserInput, UserBase
from src.security import validate_token

router = APIRouter()


@router.post("/", response_model=UserBase)
async def create_user(
    user_in: UserInput,
    db_session: DBSession,
) -> UserBase:
    user_created = crud.create_user(db_session, user_in)

    return UserBase.model_validate(user_created)


@router.get("/", response_model=list[UserBase], dependencies=[Depends(validate_token)])
async def get_users(
    db_session: DBSession,
) -> list[UserBase]:
    all_users = db_session.execute(select(User)).scalars().all()

    return [UserBase.model_validate(user) for user in all_users]
