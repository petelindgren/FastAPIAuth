# FastAPIAuth
This is a demo project use to learn new skills.

## Goals
- Follow best practices outlines in [The Twelve-Factor App](https://12factor.net/)
- Learn [Python Development Master](https://pdm.fming.dev/)
- Learn [FastAPI](https://fastapi.tiangolo.com/)
- Learn [SQL Model](https://sqlmodel.tiangolo.com/)
- Learn how to build these environments with Docker


## Set Up Development Environment
Here are some tips for setting up your local machine for development.

### Code Formatters
Install Code Formatters to help maintain a consistent look to the code.
Use pre-commit hooks to enforce code formatting checks

| Package Name | URL | Description |
|:---|:---|:---|
| autoflake | https://pypi.org/project/autoflake/ | autoflake removes unused imports and unused variables from Python code. It makes use of pyflakes to do this. |
| black | https://github.com/psf/black | |
| flake8 | https://flake8.pycqa.org/en/latest/ | Your Tool For Style Guide Enforcement. |
| isort | https://pycqa.github.io/isort/docs/configuration/pre-commit.html | Sort imports |


- Install **`pre-commit`**
  **`pre-commit`** should already be installed with `Pipfile` or `PDM` but you will still
  need to install git hooks in the `.git/` project directory.

  ```sh
  # Run this to install .pre-commit-config.yaml
  pre-commit install
  ```

  Run **`pre-commit`** on all files:

  ```sh
  pre-commit run --all-files
  ```

  Sometimes you want to **`pre-commit`** hooks because code is a work in progress

  ```sh
  git commit -m "Some comments" --no-verify
  ```


- Install **`isort`**

  ``sh
  brew install isort
  ```

  Allows you to run isort on specific files
  ```
  isort -m3 --trailing-comma -w88 docker-compose.yaml
  ```


References:
- https://py-vscode.readthedocs.io/en/latest/files/linting.html 
- https://medium.com/staqu-dev-logs/keeping-python-code-clean-with-pre-commit-hooks-black-flake8-and-isort-cac8b01e0ea1
- https://github.com/microsoft/presidio/issues/317
- https://black.readthedocs.io/en/stable/compatible_configs.html


### Setting up Mac OS

- Install brew packages

  ```sh
  brew install isort
  brew install rust
  brew install openssl@1.1
  brew install pdm
  ```


### Visual Studio Code

For convenience, build a virtual environment from the Pipfile.
This virtual environment can then be added to Visual Studio Code
Ref: https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment


### Install Python Development Master (PDM)
Documentation: https://pdm.fming.dev/

### Set up PDM
- Install PDM local environment

  ```sh
  pdm install
  ```

- Run application locally by running:

  ```sh
  pdm run python3 -m uvicorn main:app --reload
  ```

- Export `pdm.lock` packages to `requirements.txt` file

  ```sh
  pdm export -f requirements --without-hashes -o requirements.txt
  ```


## Docker
See **`examples/`** of different ways to configure `Dockerfile` and `docker-compose.yaml`
to start a FastAPI project


### Tips
- If your local Docker environment gets cluttered run this shell script
  to remove all Docker Containers, Volumes and Images

  ```sh
  ./bin/clean_up_docker_resources.sh
  ```

- If you Docker environment goes really, prune everything

  ```sh
  docker system prune -a
  ```

- Find **`site-packages`** directory in a Docker Container

  ```sh
  python -m site
  ```

### Debugging SQLite Databases

- Install [DB Browser for SQLite](https://sqlitebrowser.org/) for reading SQLite DB files

  ```sh
  brew install --cask db-browser-for-sqlite
  ```

- On Mac OS you can now find **DB Browser for SQLite** in your Applications



### Testing Dockerfile(s)

- Install [Container Structure Test](https://github.com/GoogleContainerTools/container-structure-test)

  ```sh
  brew install container-structure-test
  ```

- Run unit tests on container

  ```sh
  container-structure-test test --image docker.io/library/docker-pdm --config unit-test-dockerfile-pdm.yaml
  ```

  🔑 Use the name of the container image `docker.io/library/docker-pdm`
