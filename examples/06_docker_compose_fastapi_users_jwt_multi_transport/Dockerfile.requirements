# https://fastapi.tiangolo.com/deployment/docker/#dockerfile
FROM python:3.9-slim

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src/

# Use entrypoint to keep Docker container running for debugging
# ENTRYPOINT ["tail", "-f", "/dev/null"]

EXPOSE 8000
