# https://jonathanmeier.io/using-pipenv-with-docker/
FROM python:3.9-slim

RUN pip install pipenv

ENV PROJECT_DIR /code

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pipenv install --system --deploy

# Difference from Example 01: Copy directory instead of a single file
COPY ./hello_world ${PROJECT_DIR}/app

# Difference from Example 01: Change start path to "app.main:app"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
