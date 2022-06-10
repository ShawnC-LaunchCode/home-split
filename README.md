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