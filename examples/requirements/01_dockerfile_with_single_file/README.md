# Dockerfile with Single File FastAPI

This example demonstrates how to build and run a single file FastAPI application
with a `Dockerfile`

- Build the Docker Image

  ```sh
  docker build -t dockerfile-singlefile-image .
  ```

- Verify the Docker Image exists

  Run the following in a shell terminal

  ```sh
  docker image ls
  docker image ls | grep dockerfile-singlefile-image
  ```

  you should see something that looks like this:

  >```
  >REPOSITORY                            TAG       IMAGE ID       CREATED       SIZE
  >dockerfile-singlefile-image           latest    05d66f0ae8f0   9 hours ago   219MB
  >```

- Run the Docker Image in a Docker Container

  Run the following in a shell terminal

  ```sh
  docker run -d --name dockerfile-singlefile-container  -p 80:80 dockerfile-singlefile-image
  ```

  Troubleshooting
  
  - Error Type: The container name is already in use

    - Example Message:
  
      >docker: Error response from daemon: Conflict. The container name "/dockerfile-singlefile-container" is already in use by container "d1190b593f10475ff4b54705442decbad8ae51b93869571266be00a320200ff3". You have to remove (or rename) that container to be able to reuse that name.

    - Solution: Stop and Remove existing container

      Run the following in a shell terminal

      ```sh
      docker container stop dockerfile-singlefile-container
      docker container rm dockerfile-singlefile-container
      ```


- Verify the Docker Container is running

  Run the following in a shell terminal

  ```sh
  docker ps
  ```

  you should see something that looks like this:

  >```
  >CONTAINER ID   IMAGE                         COMMAND                  CREATED              STATUS              PORTS                NAMES
  >4d6e1f60e125   dockerfile-singlefile-image   "uvicorn main:app --…"   About a minute ago   Up About a minute   0.0.0.0:80->80/tcp   dockerfile-singlefile-container
  >```


- Go to web browser http://127.0.0.1/

  You should see this message 

  ```
  {"message":"Dockerfile version of SingleFile Hello World"}
  ```
