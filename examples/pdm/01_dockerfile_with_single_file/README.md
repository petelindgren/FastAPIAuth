# PDM Dockerfile with Single File FastAPI

This example demonstrates how to build and run a single file FastAPI application
with a `Dockerfile`


## Build an image from a Dockerfile

  Build the Docker Image

  ```sh
  docker build -t pdm-dockerfile-singlefile-image .
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/build/


## Manage images

  Verify the Docker Image exists with `ls`

  ```sh
  docker image ls
  docker image ls | grep pdm-dockerfile-singlefile-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY                        TAG       IMAGE ID       CREATED             SIZE
  >pdm-dockerfile-singlefile-image   latest    2a04273e832a   3 seconds ago       170MB
  >```


## Run a command in a new container

  Start the Docker Image in a new Container

  ```sh
  docker run -d --name pdm-dockerfile-singlefile-container -p 80:80 pdm-dockerfile-singlefile-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/run/

  **Troubleshooting**
  
  - Error Type: The container name is already in use

    Example Message:
  
    >docker: Error response from daemon: Conflict. The container name "/pdm-dockerfile-singlefile-container" is already in use by container "d1190b593f10475ff4b54705442decbad8ae51b93869571266be00a320200ff3". You have to remove (or rename) that container to be able to reuse that name.

    Solution: Stop and Remove existing container

    ```sh
    docker container stop pdm-dockerfile-singlefile-container
    docker container rm pdm-dockerfile-singlefile-container
    ```


## List containers

  Verify the Docker Container is running

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                             COMMAND                  CREATED         STATUS         PORTS                NAMES
  >a6555a3e96d5   pdm-dockerfile-singlefile-image   "python -m uvicorn p…"   3 seconds ago   Up 2 seconds   0.0.0.0:80->80/tcp   pdm-dockerfile-singlefile-container
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"message":"PDM Dockerfile version of SingleFile Hello World"}
  ```
