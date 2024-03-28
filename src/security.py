from datetime import timedelta, timezone, datetime
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src import User
from src.configurations import settings
from src.database import DBSession
from src.schemas.token import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def validate_token(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        exp = payload.get("exp")
        if username is None or exp is None:
            raise credentials_exception
        return TokenData(user_name=username, expiration=exp)
    except JWTError:
        raise credentials_exception


def get_current_user(db_session: DBSession, valid_token: TokenData = Depends(validate_token)) -> User:
    user = db_session.query(User).filter(User.username == valid_token.user_name).one()

    return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def authenticate_user(db_session: Session, username: str, password: str):
    user = db_session.query(User).filter(User.username == username).one_or_none()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
