from datetime import datetime

from fastapi import APIRouter, Depends

from src.schemas.comments import Comment
from src.security import validate_token

router = APIRouter(dependencies=[Depends(validate_token)])


@router.get("/", response_model=Comment)
async def fetch_comments_of_post(post_id: int) -> Comment:
    return Comment(
        content="abc",
        creation_time=datetime.utcnow(),
        last_modified_time=datetime.utcnow(),
    )
