# import db models, so alembic migration can detect it
from src.database.models.blogs import Blog  # noqa: F401
from src.database.models.users import User  # noqa: F401
