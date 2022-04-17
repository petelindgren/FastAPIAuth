# FastAPIAuth
This is a demo project use to learn new skills.

## Goals
- Follow best practices outlines in [The Twelve-Factor App](https://12factor.net/)
- Learn [Python Development Master](https://pdm.fming.dev/)
- Learn [FastAPI](https://fastapi.tiangolo.com/)
- Learn [SQL Model](https://sqlmodel.tiangolo.com/)
- Learn how to build these environments with Docker

## Running
- Install PDM local environment

  ```sh
  pdm install
  ```

- Run application locally by running:

  ```sh
  pdm run python3 -m uvicorn main:app --reload
  ```

## Set Up Development Environment

- Install PDM on computer

  ```sh
  brew install rust
  brew install openssl@1.1
  brew install pdm
  ```

## Docker

### Building Single File Hello World App from Dockerfile

- Building the Dockerfile

  ```sh
  docker build -f Dockerfile.singlefile -t dockerfile-singlefile-image .
  docker build -f Dockerfile.singlefile.pdm -t dockerfile-singlefile-pdm-image .
  docker build -f Dockerfile.multifile -t dockerfile-multifile-image .
  docker build -f Dockerfile.multifile.pdm -t docker-multifile-pdm-image .
  ```

- Run the Docker Image in Container

  ```sh
  docker run -d --name dockerfile-singlefile-container  -p 80:80 dockerfile-singlefile-image
  docker run -d --name dockerfile-singlefile-pdm-container -p 80:80 dockerfile-singlefile-pdm-image
  docker run -d --name dockerfile-multifile-container -p 80:80 dockerfile-multifile-image
  docker run -d --name dockerfile-multifile-pdm-container -p 80:80 docker-multifile-pdm-image
  ```

  Command Line Output

    >```
    >$ docker run -d --name dockerfile-singlefile-container  -p 80:80 dockerfile-singlefile-image
    >ae13d27c9838e29663439a86326f71eeca249e6ae07021b8e62116c8c0192a9d
    >```

- Check Single File Hello World in a web browser

  - Navigate to http://127.0.0.1/

  - Should see

    >{"message":"Single File Hello World"}

- Stop Docker Container

  ```sh
  docker container stop dockerfile-singlefile-container
  docker container stop dockerfile-singlefile-container-pdm
  docker container stop dockerfile-multifile-container
  docker container stop dockerfile-multifile-container-pdm
  ```

- Remove Docker Container

  ```sh
  docker container rm dockerfile-singlefile-container
  docker container rm dockerfile-singlefile-container-pdm
  docker container rm dockerfile-multifile-container
  docker container rm dockerfile-multifile-container-pdm
  ```

- Troubleshooting

- Check Docker Image

  ```sh
  docker image ls
  ```

  Command Line Output

    >```
    >$ docker image ls
    >REPOSITORY                    TAG       IMAGE ID       CREATED          SIZE
    >dockerfile-singlefile-image   latest    05d66f0ae8f0   46 minutes ago   219MB
    >```

- Check Docker Container

  ```sh
  docker container ls
  ```

  Command Line Output

    >```
    >$ docker container ls
    >CONTAINER ID   IMAGE                         COMMAND                  CREATED         STATUS         PORTS                NAMES
    >d194550cce39   dockerfile-singlefile-image   "uvicorn main:app --…"   3 minutes ago   Up 3 minutes   0.0.0.0:80->80/tcp   dockerfile-singlefile-container
    >```

  - SSH into the running Docker Container

    ```sh
    docker ps
    ```

    Command Line Output

    >```docker ps
    >CONTAINER ID   IMAGE                         COMMAND                  CREATED              STATUS              PORTS                NAMES
    >d194550cce39   dockerfile-singlefile-image   "uvicorn main:app --…"   About a minute ago   Up About a minute   0.0.0.0:80->80/tcp   dockerfile-singlefile-container
    >```

  - SSH into the Container

    ```sh
    docker exec -it ca459d14b296 bash
    ```

    Command Line Output

    >```
    >docker exec -it ca459d14b296 bash
    >root@ca459d14b296:/code# ls
    >__pycache__  main.py  requirements.txt
    >root@ca459d14b296:/code# less main.py 
    >```


  - Web Page does not load because **Chrome** "_This site can’t be reached_" or **Safari** "_Safari Can't Open the Page_" or **Firefox** "_Unable to connect_"

    1. Check if Docker is listen to ports in Mac OS

       ```sh
       lsof -nP -iTCP -sTCP:LISTEN
       ```

       Command Line Output

        >```
        >COMMAND    PID    USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
        >rapportd   429 packrat    6u  IPv4 0x5b74d5ede773f043      0t0  TCP *:53993 (LISTEN)
        >rapportd   429 packrat    7u  IPv6 0x5b74d5df828833ab      0t0  TCP *:53993 (LISTEN)
        >com.docke 2120 packrat  109u  IPv6 0x5b74d5df8287cc8b      0t0  TCP *:5432 (LISTEN)
        >com.docke 2120 packrat  127u  IPv6 0x5b74d5df8287a82b      0t0  TCP *:80 (LISTEN)
        >```


  - The container name "<container>" is already in use

    >docker: Error response from daemon: Conflict. The container name "/hello-world-singlefile" is already in use by container "c5bf6fcac2c3ab0abe0ffd5bd409c2fcc92c5e721528506fcaddf696dc30148b". You have to remove (or rename) that container to be able to reuse that name.

    1. Remove existing container

       ```sh
       docker container rm dockerfile-singlefile-container
       ```

       Command Line Output

        >```
        >$ docker container rm dockerfile-singlefile-container
        >dockerfile-singlefile-container
        >```

    2. Re-run the Docker Image in Container

        ```sh
        docker run -d --name dockerfile-singlefile-container dockerfile-singlefile-image
        ```

### Build Simple Hello World App from docker-compose

- Build

  ```sh
  docker-compose -f docker-compose-singlefile.yaml up -d
  docker-compose -f docker-compose-singlefile-pdm.yaml up -d
  docker-compose -f docker-compose-multifile.yaml up -d
  ```

- Stop

  ```sh
  docker-compose -f docker-compose-singlefile.yaml down
  docker-compose -f docker-compose-singlefile-pdm.yaml down
  docker-compose -f docker-compose-multifile.yaml down
  ```


## Docker

- Building the Dockerfile

  ```sh
  docker build -f Dockerfile.pdm -t docker-pdm .
  ```

  will produce an output like this:

  >```
  >➜  FastAPIAuth git:(add_dockerfile) ✗ docker build -f Dockerfile.pdm -t docker-pdm .
  >[+] Building 18.3s (13/13) FINISHED                                                   
  > => [internal] load build definition from Dockerfile.pdm                                        0.0s
  > ...
  > => [builder 7/7] RUN pdm install --prod --no-lock --no-editable                               17.2s
  > => CACHED [stage-1 2/2] COPY --from=builder /project/__pypackages__/3.9/lib /project/pkgs      0.0s 
  > => exporting to image                                                                          0.0s 
  > => => exporting layers                                                                         0.0s 
  > => => writing image sha256:9118e6d3fd678bce2530e3ef47422deefe53e4b8e20fe257adf414cf0d627edb    0.0s 
  > => => naming to docker.io/library/docker-pdm                                                   0.0s 
  >```

  🔑 The name of the image is used for testing the container `docker.io/library/docker-pdm`

- Find existing Dockerfile images

  ```docker image ls
  REPOSITORY                TAG       IMAGE ID       CREATED             SIZE
  docker-pdm                latest    9118e6d3fd67   About an hour ago   988MB
  ```

### Testing Dockerfile(s)

- Install [Container Structure Test](https://github.com/GoogleContainerTools/container-structure-test)

  ```sh
  brew install container-structure-test
  ```

- Run unit tests on container

  ```sh
  container-structure-test test --image docker.io/library/docker-pdm --config unit-test-dockerfile-pdm.yaml
  ```

  🔑 Use the name of the container image `docker.io/library/docker-pdm`
