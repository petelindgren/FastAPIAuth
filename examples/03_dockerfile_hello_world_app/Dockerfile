# https://pdm-project.org/en/latest/usage/advanced/#use-pdm-in-a-multi-stage-dockerfile
# https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-with-a-single-file-fastapi

# build stage
FROM python:3.12-slim AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy PDM files to project
COPY pyproject.toml pdm.lock README.md /project/

# install dependencies and project
WORKDIR /project
RUN pdm install --prod --no-lock --no-editable

# run stage
FROM python:3.12-slim

ENV PYTHONPATH=/project/pkgs
ENV PACKAGE_MANAGER_NAME=PDM

# retrieve packages from build stage
COPY --from=builder /project/__pypackages__/3.9/lib /project/pkgs

# copy project files
COPY ./src /project/src

WORKDIR /project

# set command/entrypoint, adapt to fit your needs
ENTRYPOINT ["python", "-m"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
