from fastapi import APIRouter, Depends

from src import crud
from src.database import User
from src.database.dependencies import DBSession
from src.schemas.blogs import BlogCreate, BlogDTO, BlogInDB
from src.security import get_current_user

router = APIRouter()


@router.get("/", response_model=list[BlogDTO])
async def get_your_blogs(
    db_session: DBSession, current_active_user: User = Depends(get_current_user)
) -> list[BlogDTO]:
    all_blogs = crud.get_blogs_by_user_id(db_session, current_active_user.id)
    return [BlogDTO.model_validate(blog) for blog in all_blogs]


@router.post("/", response_model=BlogDTO)
async def create_blog(
    blog: BlogCreate,
    db_session: DBSession,
    current_active_user: User = Depends(get_current_user),
) -> BlogDTO:
    blog_for_creation = BlogInDB(
        title=blog.title,
        content=blog.content,
        owner_id=current_active_user.id,
    )

    created_blog = crud.create_blog(db_session, blog_for_creation)

    return BlogDTO.model_validate(created_blog)
