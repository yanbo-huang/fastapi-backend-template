from fastapi import FastAPI

from src.routers import blogs, users, token

app = FastAPI()

app.include_router(blogs.router, prefix="/blogs", tags=["blogs"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(token.router, prefix="/token", tags=["token"])
