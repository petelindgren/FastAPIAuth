# FastAPI Users

Run FastAPI Users SQLAlchemy example with `docker-compose.yaml` and a `Dockerfile`
using two different combinations of Transport + Strategy:
- Bearer Token Transport and JWT Strategy
- Cookie Transport and DB Strategy

This FastAPI application uses **`sqlite`** to power the database.

This Example 8 has been changed from Example 7
* Refactor the declarative `Base`
* Use a **`sqlite`** DB Strategy


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
  >CONTAINER ID   IMAGE                    COMMAND            CREATED         STATUS          PORTS                  NAMES
  >d584605aaf36   pipenv-example08-image   "python -m main"   2 minutes ago   Up 40 seconds   0.0.0.0:80->8000/tcp   pipenv-example08-container
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
  >REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
  >pipenv-example08-image   latest    25d6b8171f89   3 minutes ago    288MB
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/image/


## Verify FastAPI is running with a Web Browser

  Go to web browser http://localhost/

  You should see this

  ```
  {"root":"Analog Interface"}
  ```
