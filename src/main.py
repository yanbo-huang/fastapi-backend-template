from fastapi import FastAPI

from src.routers import posts, users, token

app = FastAPI()

app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(token.router, prefix="/token", tags=["token"])
