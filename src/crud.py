from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.orm import Session

from src import Blog, User
from src.schemas.blogs import BlogInDB
from src.schemas.user import UserInput
from src.security import get_password_hash, verify_password


class CRUD:
    def create_user(self, db_session: Session, user_in: UserInput) -> User:
        hashed_password = get_password_hash(user_in.password)
        user_created = User(
            username=user_in.username,
            email=user_in.email,
            hashed_password=hashed_password,
        )
        db_session.add(user_created)
        db_session.commit()
        db_session.refresh(user_created)

        return user_created

    def get_all_users(self, db_session: Session) -> list[User]:
        return db_session.execute(select(User)).scalars().all()

    def authenticate_user(
        self, db_session: Session, username: str, password: str
    ) -> User | bool:
        user = db_session.query(User).filter(User.username == username).one_or_none()
        if not user:
            return False
        if not verify_password(password, user.hashed_password):
            return False
        return user

    def create_blog(self, db_session: Session, blog_in: BlogInDB) -> Blog:
        blog_created = Blog(**jsonable_encoder(blog_in))
        db_session.add(blog_created)
        db_session.commit()
        db_session.refresh(blog_created)

        return blog_created

    def get_blogs_by_user_id(self, db_session: Session, user_id: int) -> list[Blog]:
        query = select(Blog).join(User).where(User.id == user_id)
        return db_session.execute(query).scalars().all()


crud = CRUD()
