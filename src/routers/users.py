from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import DBSession, get_db_session
from src.models.users import User
from src.schemas.user import UserInput, UserBase
from src.security import get_password_hash

router = APIRouter()


@router.post("/", response_model=UserBase)
async def create_user(
        user_in: UserInput,
        db_session: Session = Depends(get_db_session),
) -> UserBase:
    hashed_password = get_password_hash(user_in.password)
    user_create = User(username=user_in.username, email=user_in.email, hashed_password=hashed_password)
    db_session.add(user_create)
    db_session.commit()

    return UserBase.model_validate(user_create)
