# Dockerfile with a FastAPI Project

This example demonstrates how to build and run a FastAPI application using a directory structure
with a `Dockerfile`


## Build an image from a Dockerfile

  Use PDM Dockerfile to build Docker Image `pdm-example03-image`

  ```sh
  docker build -t pdm-example03-image .
  ```

  or build one of the other Dockerfiles

  ```sh
  docker build -f Dockerfile.pipenv -t pipenv-example03-image .
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/build/


## Manage images

  Verify the Docker Image `pdm-example03-image` exists with `ls`

  ```sh
  docker image ls
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY               TAG       IMAGE ID       CREATED          SIZE
  >pipenv-example03-image   latest    94b8d0655ba1   12 seconds ago   239MB
  >pdm-example03-image      latest    34662b2599db   42 seconds ago   170MB
  >```


## Run a command in a new container

  Start the different Docker Images in a new Container

  ```sh
  docker run --name pdm-example03-container -p 80:80 pdm-example03-image
  docker run --name pipenv-example03-container -p 80:80 pipenv-example03-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/run/

  **Troubleshooting**
  
  - Error Type: The container name is already in use

    Example Message:
  
    >docker: Error response from daemon: Conflict. The container name "/pdm-example03-container" is already in use by container "d1190b593f10475ff4b54705442decbad8ae51b93869571266be00a320200ff3". You have to remove (or rename) that container to be able to reuse that name.

    Solution: Stop and Remove existing container

    ```sh
    docker container stop pdm-example03-container
    docker container rm pdm-example03-container
    ```


## List containers

  Verify the Docker Container is running

  ```sh
  docker ps
  ```

  or

  ```sh
  docker container ls
  ```

  >```
  >CONTAINER ID   IMAGE                 COMMAND                  CREATED          STATUS          PORTS                NAMES
  >8f687f488fed   pdm-example03-image   "python -m uvicorn s…"   44 seconds ago   Up 43 seconds   0.0.0.0:80->80/tcp   pdm-example03-container
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/



## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  Depending on which Dockerfile you chose to build and run
  you will see one of these responses:

  ```
  {"root":"Analog Interface (PDM)"}
  ```

  or

  ```
  {"root":"Analog Interface (Pipenv)"}
  ```
