# Dockerfile with Single File FastAPI

This example demonstrates how to build and run a single file FastAPI application
with a `Dockerfile`

For demonstration purposes, this example includes 3 different
ways to build the Dockerfile


## Build an image from a Dockerfile

  Use _requirements_ Dockerfile to build Docker Image `pdm-example01-image`

  ```sh
  docker build -t pdm-example01-image .
  ```

  Or build one of the other Dockerfiles

  ```sh
  docker build -f Dockerfile.pipenv -t pipenv-example01-image .
  ```

  ```sh
  docker build -f Dockerfile.requirements -t req-example01-image .
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/build/


## Manage images

  Verify the Docker Images exist with `ls`

  ```sh
  docker image ls
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
  >req-example01-image      latest    e090765c458e   7 seconds ago    179MB
  >pipenv-example01-image   latest    a68265aafdd6   12 seconds ago   247MB
  >pdm-example01-image      latest    a4a64fb160b4   3 minutes ago    170MB
  >```


## Run a command in a new container

  Start the different Docker Images in a new Container

  ```sh
  docker run --name pdm-example01-container -p 80:80 pdm-example01-image
  docker run --name pipenv-example01-container -p 80:80 pipenv-example01-image
  docker run --name req-example01-container -p 80:80 req-example01-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/run/

  **Troubleshooting**
  
  - Error Type: The container name is already in use

    Example Message:
  
    >docker: Error response from daemon: Conflict. The container name "/pdm-example01-container" is already in use by container "d1190b593f10475ff4b54705442decbad8ae51b93869571266be00a320200ff3". You have to remove (or rename) that container to be able to reuse that name.

    Solution: Stop and Remove existing container

    ```sh
    docker container stop pdm-example01-container
    docker container rm pdm-example01-container
    ```


## List containers

  Verify the Docker Container is running

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                 COMMAND                  CREATED         STATUS         PORTS                NAMES
  >46ee5ebab36c   pdm-example01-image   "python -m uvicorn p…"   8 seconds ago   Up 8 seconds   0.0.0.0:80->80/tcp   pdm-example01-container
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  Depending on which Dockerfile, you chose to build and run
  you will see one of these responses:

  ```
  {"message":"PDM Dockerfile version of SingleFile Hello World"}
  ```

  or

  ```
  {"message":"Pipenv Dockerfile version of SingleFile Hello World"}
  ```

  or

  ```
  {"message":"Requirements Dockerfile version of SingleFile Hello World"}
  ```
