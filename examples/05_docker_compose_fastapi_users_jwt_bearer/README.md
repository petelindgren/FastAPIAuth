# FastAPI Users

Run FastAPI Users SQLAlchemy example with `docker-compose.yaml` and a `Dockerfile`
using Bearer Token transport with JWT Strategy.

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

  Verify the Docker Container named `pipenv-example05-container` is running with `ps`

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                    COMMAND            CREATED         STATUS          PORTS                  NAMES
  >e7fb5bb96fb6   pipenv-example05-image   "python -m main"   5 minutes ago   Up 46 seconds   0.0.0.0:80->8000/tcp   pipenv-example05-container
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/


## Stops containers and removes containers, networks, volumes, and images created by up.

  ```sh
  docker-compose down -v
  ```

  Reference: https://docs.docker.com/compose/reference/down/


## Manage images

  Verify the Docker Image `pipenv-example05-image` exists with `ls`

  ```sh
  docker image ls
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
  >pipenv-example05-image   latest    1add01b41b16   8 minutes ago    288MB
  >```


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"detail":"Not Found"}
  ```
