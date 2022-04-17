# Dockerfile with Multi File FastAPI App

This example demonstrates how to build and run a single file FastAPI application
with a `Dockerfile`


## Build an image from a Dockerfile

  Build the Docker Image

  ```sh
  docker build -t dockerfile-multifile-image .
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/build/


## Manage images

  Verify the Docker Image exists with `ls`

  ```sh
  docker image ls
  docker image ls | grep dockerfile-multifile-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/image/

  >```
  >REPOSITORY                        TAG       IMAGE ID       CREATED          SIZE
  >dockerfile-multifile-image        latest    1036351ef505   4 minutes ago    179MB
  >```


## Run a command in a new container

  Start the Docker Image in a new Container

  ```sh
  docker run -d --name dockerfile-multifile-container  -p 80:80 dockerfile-multifile-image
  ```

  Reference: https://docs.docker.com/engine/reference/commandline/run/

  **Troubleshooting**
  
  - Error Type: The container name is already in use

    Example Message:
  
    >docker: Error response from daemon: Conflict. The container name "/dockerfile-multifile-container" is already in use by container "d1190b593f10475ff4b54705442decbad8ae51b93869571266be00a320200ff3". You have to remove (or rename) that container to be able to reuse that name.

    Solution: Stop and Remove existing container

    ```sh
    docker container stop dockerfile-multifile-container
    docker container rm dockerfile-multifile-container
    ```


## List containers

  Verify the Docker Container is running

  ```sh
  docker ps
  ```

  >```
  >CONTAINER ID   IMAGE                         COMMAND                  CREATED              STATUS              PORTS                NAMES
  >4d6e1f60e125   dockerfile-multifile-image   "uvicorn main:app --…"   About a minute ago   Up About a minute   0.0.0.0:80->80/tcp   dockerfile-multifile-container
  >```

  Reference: https://docs.docker.com/engine/reference/commandline/ps/


## Verify FastAPI is running with a Web Browser

  Go to web browser http://127.0.0.1/

  You should see this

  ```
  {"Hello":"World from MultiFile Dockerfile"}
  ```
