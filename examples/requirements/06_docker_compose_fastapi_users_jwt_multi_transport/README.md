# FastAPI Users

Run FastAPI Users SQLAlchemy example with `docker-compose.yaml` and a `Dockerfile`
using Bearer Token or Cookie transport with JWT Strategy

This FastAPI application uses **`sqlite`** to power the database.

References:
- https://github.com/fastapi-users/fastapi-users/tree/v10.0.2/examples/sqlalchemy

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

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                    COMMAND            CREATED          STATUS          PORTS                  NAMES
  >2bfae674bbdd   pipenv-example06-image   "python -m main"   15 seconds ago   Up 14 seconds   0.0.0.0:80->8000/tcp   pipenv-example06-container
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
  ```

  >```
  >REPOSITORY               TAG       IMAGE ID       CREATED             SIZE
  >pipenv-example06-image   latest    322a82feb672   34 seconds ago      288MB
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/image/


## Verify FastAPI is running with a Web Browser

  Go to web browser http://localhost/

  You should see this

  ```
  {"detail":"Not Found"}
  ```
