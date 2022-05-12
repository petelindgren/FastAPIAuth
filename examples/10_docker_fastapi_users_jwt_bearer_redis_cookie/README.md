# FastAPI Users

Run FastAPI Users SQLAlchemy example with `docker-compose.yaml` and a `Dockerfile`
using two different combinations of Transport + Strategy:
- Bearer Token Transport and JWT Strategy
- Cookie Transport and DB Strategy

This FastAPI application uses **`sqlite`** to power the database.

This Example 9 has been changed from Example 8
* Use a **`postgres`** DB Strategy


References:
- https://github.com/fastapi-users/fastapi-users/tree/v10.0.2/examples/sqlalchemy

## Builds, (re)creates, starts, and attaches to containers for a service.

  Build Docker Image with PDM

  ```sh
  docker-compose up --build
  ```

  Build Docker Image with Pipenv

  ```sh
  docker-compose -f docker-compose-pipenv.yml up --build
  ```

  Optional: Build image and run container _detached_

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

  List existing Docker Images with `ls` and compare size of PDM and Pipenv images

  ```sh
  docker image ls
  ```

  >```
  >REPOSITORY               TAG           IMAGE ID       CREATED          SIZE
  >pipenv-example09-image   latest        61396c93df45   11 seconds ago   288MB
  >pdm-example09-image      latest        c77dac16f9f1   59 seconds ago   193MB
  >postgres                 13.6-alpine   928a7a35a1ad   4 weeks ago      207MB
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/image/


## Verify FastAPI is running with a Web Browser

  Go to web browser http://localhost/

  You should see this

  ```
  {"root":"Analog Interface (PDM)"}
  ```

  or 

  ```
  {"root":"Analog Interface (Pipenv)"}
  ```

## Connect to Docker Postgresql

1.  Get the Container ID above with `docker ps`

2.  Log into the Docker container for postgres

    ```
    docker exec -it 5daf303c9e25 bash
    ```

3.  Connect to `psql`

    ```sh
    psql -h localhost -U example9
    ```

    - This is why the username and DB are the same
