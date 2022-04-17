# PDM docker-compose with Single File FastAPI

This example demonstrates how to build and run a single file FastAPI application
using `docker-compose.yaml` and a `Dockerfile`


## Builds, (re)creates, starts, and attaches to containers for a service.

  ```sh
  docker-compose up -d
  ```

   Reference: https://docs.docker.com/compose/reference/up/


## List Docker containers

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS          PORTS                  NAMES
  >a1bc42c5c4d4   pdm-docker-compose-singlefile-image   "python -m uvicorn p…"   23 seconds ago   Up 21 seconds   0.0.0.0:80->8000/tcp   02_docker_compose_with_single_file_api_1
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/


## Stops containers and removes containers, networks, volumes, and images created by up.

  ```sh
  docker-compose down
  ```

  Reference: https://docs.docker.com/compose/reference/down/


## Manage images

  Verify the Docker Image exists with `ls`

  ```sh
  docker image ls
  docker image ls | grep pdm-docker-compose-singlefile-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY                            TAG       IMAGE ID       CREATED          SIZE
  >pdm-docker-compose-singlefile-image   latest    6f306c98d601   41 seconds ago   170MB
  >```


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"message":"PDM docker-compose version of SingleFile Hello World"}
  ```
