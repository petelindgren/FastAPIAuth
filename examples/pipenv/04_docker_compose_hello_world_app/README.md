# docker-compose with FastAPI Project

This example demonstrates how to build and run a FastAPI application using a directory structure
using `docker-compose.yaml` and a `Dockerfile`


## Builds, (re)creates, starts, and attaches to containers for a service.

  ```sh
  docker-compose up --build
  ```

  or run _detached_

  ```sh
  docker-compose up -d --build
  ```

   Reference: https://docs.docker.com/compose/reference/up/


## List Docker containers

  Verify the Docker Container named `pipenv-example04-container` is running with `ps`

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                  NAMES
  >4a9fc231cb01   pipenv-example04-image   "uvicorn app.main:ap…"   14 seconds ago   Up 13 seconds   0.0.0.0:80->8000/tcp   pipenv-example04-container
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/


## Stops containers and removes containers, networks, volumes, and images created by up.

  ```sh
  docker-compose down -v
  ```

  Reference: https://docs.docker.com/compose/reference/down/


## Manage images

  Verify the Docker Image `pipenv-example04-image` exists with `ls`

  ```sh
  docker image ls
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY                 TAG       IMAGE ID       CREATED              SIZE
  >pipenv-example04-image     latest    1a5b5d220b09   About a minute ago   247MB
  >```


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"Hello": "World from MultiFile docker-compose"}
  ```
