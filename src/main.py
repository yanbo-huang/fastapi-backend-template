from fastapi import FastAPI

from src.routers import posts, comments

app = FastAPI()

app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])
