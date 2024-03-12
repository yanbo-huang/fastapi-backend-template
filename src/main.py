from fastapi import FastAPI

from src.routers import posts, comments, token

app = FastAPI()

app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])
app.include_router(token.router, prefix="/token", tags=["token"])
