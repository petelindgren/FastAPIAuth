# Dockerfile with a FastAPI Project

This example demonstrates how to build and run a FastAPI application using a directory structure
with a `Dockerfile`


## Build an image from a Dockerfile

  Build the Docker Image `dockerfile-project-image`

  ```sh
  docker build -t dockerfile-project-image .
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/build/


## Manage images

  Verify the Docker Image `dockerfile-project-image` exists with `ls`

  ```sh
  docker image ls
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY                 TAG       IMAGE ID       CREATED          SIZE
  >dockerfile-project-image   latest    efbcb8a7c9b3   6 seconds ago    247MB
  >```


## Run a command in a new container

  Start the Docker Image `dockerfile-project-image` in a new Container `dockerfile-project-container`

  ```sh
  docker run -d --name dockerfile-project-container -p 80:80 dockerfile-project-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/run/

  **Troubleshooting**
  
  - Error Type: The container name is already in use

    Example Message:
  
    >docker: Error response from daemon: Conflict. The container name "/dockerfile-project-container" is already in use by container "d1190b593f10475ff4b54705442decbad8ae51b93869571266be00a320200ff3". You have to remove (or rename) that container to be able to reuse that name.

    Solution: Stop and Remove existing container

    ```sh
    docker container stop dockerfile-project-container
    docker container rm dockerfile-project-container
    ```


## List containers

  Verify the Docker Container is running

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                         COMMAND                  CREATED              STATUS              PORTS                NAMES
  >4d6e1f60e125   dockerfile-project-image   "uvicorn main:app --…"   About a minute ago   Up About a minute   0.0.0.0:80->80/tcp   dockerfile-project-container
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"Hello":"World from MultiFile Dockerfile"}
  ```
