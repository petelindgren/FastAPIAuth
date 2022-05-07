# https://fastapi.tiangolo.com/deployment/docker/#dockerfile
FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./hello_world /code/app

EXPOSE 8000
