FROM python:3.12-slim
USER root

WORKDIR /opt/project

# Unset because of https://github.com/psf/requests/issues/3829
ENV REQUESTS_CA_BUNDLE=
# Ignore warnings during requests calls
ENV PYTHONWARNINGS="ignore:Unverified HTTPS request"

ENV MOCK_HOSTNAME=api-mock-server
ENV PYTHONPATH="/opt/project"

RUN pip install poetry

# Installing dependencies and setup poetry env
COPY poetry.lock        /opt/project/poetry.lock
COPY pyproject.toml     /opt/project/pyproject.toml
RUN poetry config virtualenvs.in-project true
RUN poetry config virtualenvs.options.no-pip true
RUN poetry install
