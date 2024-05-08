# fastapi-backend-template 
A template based on Copier for building a FastAPI backend project including only the essential/minimal components.


### What are the essential backend components in this template?

- `FastAPI`: REST API
- `JWT`: authentication
- `Postgresql`: relational database
- `SQLAlchemy`: ORM
- `Alembic`: schema migration
- `Pydantic`: data modeling and validation
- `Poetry`: dependency management
- `Black, Ruff, ...`: linting tools
- `pre-commit`: git pre commit hooks
- `dotenv, Pydantic-settings`: configuration management
- `Docker`: containerization
- `Docker Compose`: orchestration

### How to use the template?

#### Install Copier

Install Copier using pipx.
> Note: it is encouraged to use pipx to install wildly used CLI library. This way, you can have libraries installed in separate environment but use them as a global way.
If you don't have pipx, install it by following [pipx installing](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx)
```shell
pipx install copier
```

#### Generate a project from the template

> Note: `--trust` is necessary here to run a post task to create the `.env` file for you.
```shell
copier copy https://github.com/yanbo-huang/fastapi-backend-template <your local project path> --trust
```

Answer the questions to customize your project, then you have a **_battery-included_** project ready.

That's easy, right? :-)

Check your local README.md to see how to start everything. Have fun with building your awesome project!

