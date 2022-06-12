# HOME-SPLIT
## Getting started

### Install Dependencies
1. **Poetry** - for package dependency management.

https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions

1. **Docker** - for required services, like mysql

https://docs.docker.com/desktop/windows/install/

### Set up Python environment
Run:
```bash
poetry install
poetry shell
```

### Run the app
Run:
```bash
docker-compose up # for the database
uvicorn --reload app.helloworld:app --host 0.0.0.0 --port 8000
```
## Installing new Python packages
1. Add the package via Poetry
``` bash
poetry add <some-new-awesome-package>
```

## Useful commands
Start a poetry shell
```bash
poetry shell
```

## Modifying the database schema
1. Make your update in `app/modeils.py`
2. Run `alembic revision --autogenerate -m "init"`
3. Doublecheck the new migration file generated in `migrations/versions`
4. Run `alembic upgrade head`