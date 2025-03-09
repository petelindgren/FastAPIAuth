# https://pdm-project.org/en/latest/usage/advanced/#use-pdm-in-a-multi-stage-dockerfile
# https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-with-a-single-file-fastapi

# build stage
FROM python:3.9-slim AS builder

# set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /project

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy PDM files to project
COPY pyproject.toml pdm.lock README.md /project/

# install dependencies and project
RUN pdm install --prod --no-lock --no-editable

# run stage
FROM python:3.9-slim

ENV PYTHONPATH=/project/pkgs
# ENV PACKAGE_MANAGER_NAME=PDM

# retrieve packages from build stage
COPY --from=builder /project/__pypackages__/3.9/lib /project/pkgs

# copy project files
COPY ./src /project/src

WORKDIR /project

EXPOSE 8000
