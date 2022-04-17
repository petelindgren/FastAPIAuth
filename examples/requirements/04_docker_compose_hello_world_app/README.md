# docker-compose with Single File FastAPI

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
  >CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS          PORTS                  NAMES
  >819523e5d9e0   docker-compose-multifile-image   "uvicorn app.main:ap…"   27 seconds ago   Up 26 seconds   0.0.0.0:80->8000/tcp   04_docker_compose_hello_world_app_api_1
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
  docker image ls | grep docker-compose-multifile-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY                        TAG       IMAGE ID       CREATED          SIZE
  >docker-compose-multifile-image    latest    63ce511ac655   33 minutes ago   179MB
  >```


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"Hello":"World from MultiFile docker-compose"}
  ```