# fastapi-backend-template 

A template generator to help you create a FastAPI backend project faster, which includes only the essential/minimal components.

Creating a "hello world" Fastapi application is fairly easy. But for people who want to have a proper web backend setup, there are so many configurations, micro decisions, back-and-forth debugging to just make everything running.
For example, it could easily cost you few hours to setup your ORM `SQLAlchemy` and schema migration tool `Alembic` to make it fully work. The goal of this template generator is to save your time from all those boilerplates, then you can focus on implementing the really business logics

There are already some nice full stack Fastapi templates available. Here, I will focus on the essential components which can help you quickly build a Backend application.

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
> Note: it is encouraged to use pipx to install your wildly-used CLI library. This way, you can have libraries installed in separate environments but in the meantime use them as a global way.
If you don't have pipx, install it by following [pipx installing guilde](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx)
```shell
pipx install copier
```

or (if you really don't want to use `pipx`)

```shell
pip install copier
```

#### Generate a project from the template

> Note: `--trust` is necessary here to run a post task to create the `.env` file for you.
```shell
copier copy https://github.com/yanbo-huang/fastapi-backend-template <your local project path> --trust
```

Answer the questions to customize your project, then you have a **_battery-included_** project ready.

That's easy, right? :-)

Check your local README.md to see how to start everything. Have fun with building your awesome project!

