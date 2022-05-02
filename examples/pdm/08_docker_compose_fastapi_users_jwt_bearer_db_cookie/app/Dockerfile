# https://pdm.fming.dev/usage/advanced/#use-pdm-in-a-multi-stage-dockerfile
# https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-with-a-single-file-fastapi

# build stage
FROM python:3.9-slim AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy PDM files to project src
COPY pyproject.toml pdm.lock /src/

# install dependencies and project
WORKDIR /src
RUN pdm install --prod --no-lock --no-editable

# run stage
FROM python:3.9-slim

# retrieve packages from build stage
ENV PYTHONPATH=/src/pkgs
COPY --from=builder /src/__pypackages__/3.9/lib /src/pkgs

# copy project files
COPY . /src/

# Set WORKDIR for run stage so app can be started by `python -m main`
WORKDIR /src

# set command/entrypoint, adapt to fit your needs
EXPOSE 8000
