# https://pdm-project.org/en/latest/usage/advanced/#use-pdm-in-a-multi-stage-dockerfile
# https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-with-a-single-file-fastapi

ARG PYTHON_BASE=3.12-slim

# build stage
FROM python:$PYTHON_BASE AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install -U pdm

# disable update check
ENV PDM_CHECK_UPDATE=false

# copy PDM files to project
COPY pyproject.toml pdm.lock README.md /project/

# install dependencies and project into the local packages directory
WORKDIR /project
RUN pdm install --check --prod --no-editable
RUN pdm install --check --prod --no-lock --no-editable

# run stage
FROM python:$PYTHON_BASE

# retrieve packages from build stage
COPY --from=builder /project/.venv/ /project/.venv
ENV PATH="/project/.venv/bin:$PATH"

# copy project files
COPY ./main_pdm.py /project/main.py

# set command/entrypoint, adapt to fit your needs
ENTRYPOINT ["python", "-m"]
CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "80"]
