from fastapi import APIRouter, Depends

from src.schemas.posts import PostCreate
from src.security import validate_token

router = APIRouter(dependencies=[Depends(validate_token)])


@router.get("/")
async def read_posts():
    return [{"name": "post1", "comments": []}, {"name": "post1", "comments": []}]


@router.post("/", response_model=PostCreate)
async def create_post(post: PostCreate) -> PostCreate:
    return post
