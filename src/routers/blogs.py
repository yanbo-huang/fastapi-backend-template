from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select

from src import User, Blog
from src.database import DBSession
from src.schemas.blogs import BlogDTO, BlogCreate, BlogInDB
from src.security import get_current_user

router = APIRouter()


@router.get("/", response_model=list[BlogDTO])
async def get_your_blogs(
        db_session: DBSession,
        current_active_user: User = Depends(get_current_user)
) -> list[BlogDTO]:
    all_blogs = db_session.execute(
        select(Blog).join(User).where(User.id == current_active_user.id)
    ).scalars().all()

    return [BlogDTO.model_validate(blog) for blog in all_blogs]


@router.post("/", response_model=BlogDTO)
async def create_blog(
        blog: BlogCreate,
        db_session: DBSession,
        current_active_user: User = Depends(get_current_user)
) -> BlogDTO:
    blog = BlogInDB(
        title=blog.title,
        content=blog.content,
        owner_id=current_active_user.id,
    )

    blog_object = Blog(**jsonable_encoder(blog))

    db_session.add(blog_object)
    db_session.commit()
    db_session.refresh(blog_object)

    return BlogDTO.model_validate(blog_object)




