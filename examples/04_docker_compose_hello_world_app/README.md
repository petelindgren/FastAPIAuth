# docker-compose with FastAPI Project

This example demonstrates how to build and run a FastAPI application using a directory structure
using `docker-compose.yaml` and a `Dockerfile`

For demonstration purposes, this example includes 2 different
ways to build a `Dockerfile` with `docker-compose`

## Builds, (re)creates, starts, and attaches to containers for a service.

  Use Dockerfile to build Docker Image `pdm-example04-image`

  ```sh
  docker-compose up --build
  ```

  or 

    ```sh
  docker-compose -f docker-compose-pipenv.yml up --build
  ```

   Reference: https://docs.docker.com/compose/reference/up/


## List Docker containers

  Verify the Docker Container named `pipenv-example04-container` is running with `ps`

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                  NAMES
  >81df4bde94e5   pipenv-example04-image   "uvicorn main:app --…"   24 seconds ago   Up 23 seconds   0.0.0.0:80->8000/tcp   pipenv-example04-container
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
  >REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
  >pipenv-example04-image   latest    365992878f9b   2 minutes ago   247MB
  >```


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"root":"Analog Interface (PDM)"}
  ```

  or 

  ```
  {"root":"Analog Interface (Pipenv)"}
  ```
