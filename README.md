# fastapi-backend-template
Cookiecutter template for building a FastAPI backend project including only the essential/minimal components.


### What are the essential components in this template?

- `FastAPI`: REST API

- `JWT`: authentication
- `Postgresql`: relational database
- `SQLAlchemy`: ORM
- `Alembic`: schema migration
- `Pydantic`: data modeling and validation
- `Poetry`: dependency management
- `Black, Ruff, ...`: linting tools
- `dotenv, Pydantic-settings`: configuration management
- `Docker`: containerization
- `Docker Compose`: orchestration

### How to run?

#### create configurations

> change your secrets
```shell
cp local.env .env
```

#### start Postgres database
```shell
docker-compose up --build db
```

#### run DB migration
```shell
alembic upgrade head
```


#### run the app
```shell
uvicorn src.main:app --reload
```

