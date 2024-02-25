from fastapi import APIRouter

from src.schemas.posts import PostCreate

router = APIRouter()


@router.get("/")
async def read_posts():
    return [{"name": "post1", "comments": []}, {"name": "post1", "comments": []}]


@router.post("/", response_model=PostCreate)
async def create_post(post: PostCreate) -> PostCreate:
    return post
