# HOME-SPLIT
## Getting started
### 1. Install Poetry
Poetry is required for package dependency management.

**Install:** https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions

### 2. Initialize Poetry
Run:
```bash
poetry init
```

## Run the app
Run:
```bash
uvicorn --reload app.helloworld:app --host 0.0.0.0 --port 8000
```
## Install new Python packages
1. Add the package via Poetry
``` bash
poetry add <some-new-awesome-package>
```

## Useful commands
Start a poetry shell
```bash
poetry shell
```