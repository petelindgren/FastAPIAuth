# https://jonathanmeier.io/using-pipenv-with-docker/
FROM python:3.9-slim

RUN pip install pipenv

ENV PROJECT_DIR /code

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pipenv install --system --deploy

COPY ./hello_world ${PROJECT_DIR}/app

# This is the only difference from Example 03
EXPOSE 8000
