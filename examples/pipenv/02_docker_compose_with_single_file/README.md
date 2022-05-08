# docker-compose with Single File FastAPI

This example demonstrates how to build and run a single file FastAPI application
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

  Verify the Docker Container named `pipenv-example02-container` is running with `ps`

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                  NAMES
  >81df4bde94e5   pipenv-example02-image   "uvicorn main:app --…"   24 seconds ago   Up 23 seconds   0.0.0.0:80->8000/tcp   pipenv-example02-container
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/


## Stops containers and removes containers, networks, volumes, and images created by up.

  ```sh
  docker-compose down -v
  ```

  Reference: https://docs.docker.com/compose/reference/down/


## Manage images

  Verify the Docker Image `pipenv-example02-image` exists with `ls`

  ```sh
  docker image ls
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
  >pipenv-example02-image   latest    365992878f9b   2 minutes ago   247MB
  >```


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"message": "docker-compose version of SingleFile Hello World"}
  ```
