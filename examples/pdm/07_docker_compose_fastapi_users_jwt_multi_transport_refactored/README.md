# FastAPI Users

Run FastAPI Users SQLAlchemy example with `docker-compose.yaml` and a `Dockerfile`
using two different Transport + Strategy approachs
- Bearer Token Transport and JWT Strategy
- Cookie Transport and DB Strategy

References:
- https://fastapi-users.github.io/fastapi-users/configuration/full-example/#sqlalchemy
- https://github.com/fastapi-users/fastapi-users/tree/master/examples/sqlalchemy

## Run Application with PDM

  ```sh
  pdm run python3 -m uvicorn app.app:app --reload
  ```

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
  >CONTAINER ID   IMAGE                                                  COMMAND            CREATED         STATUS         PORTS                  NAMES
  >8ee6da49059c   pdm-docker-compose-fastapi-users-jwt-multi-transport   "python -m main"   4 seconds ago   Up 2 seconds   0.0.0.0:80->8000/tcp   06_docker_compose_fastapi_users_jwt_multi_transport_api_1
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
  >REPOSITORY                                             TAG       IMAGE ID       CREATED          SIZE
  >pdm-docker-compose-fastapi-users-jwt-multi-transport   latest    edc9b2c09781   55 seconds ago   193MB
  >```


## Verify FastAPI is running with a Web Browser

  Go to web browser http://localhost/

  If started with PDM, open http://localhost:8000/

  You should see this

  ```
  {"detail":"Not Found"}
  ```
