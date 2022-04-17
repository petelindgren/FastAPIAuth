# FastAPIAuth
This is a demo project use to learn new skills.

## Goals
- Follow best practices outlines in [The Twelve-Factor App](https://12factor.net/)
- Learn [Python Development Master](https://pdm.fming.dev/)
- Learn [FastAPI](https://fastapi.tiangolo.com/)
- Learn [SQL Model](https://sqlmodel.tiangolo.com/)
- Learn how to build these environments with Docker


## Set Up Development Environment

- Install PDM on computer

  ```sh
  brew install rust
  brew install openssl@1.1
  brew install pdm
  ```


### Set up PDM
- Install PDM local environment

  ```sh
  pdm install
  ```

- Run application locally by running:

  ```sh
  pdm run python3 -m uvicorn main:app --reload
  ```


## Docker
See **`examples/`** of different ways to configure `Dockerfile` and `docker-compose.yaml`
to start a FastAPI project


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
