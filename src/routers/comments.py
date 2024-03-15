from datetime import datetime

from fastapi import APIRouter

from src.schemas.comments import Comment

router = APIRouter()


@router.get("/", response_model=Comment)
async def fetch_comments_of_post(post_id: int) -> Comment:
    return Comment(
        content="abc",
        creation_time=datetime.utcnow(),
        last_modified_time=datetime.utcnow(),
    )
