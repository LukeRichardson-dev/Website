FROM python:3.10-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app/

FROM base AS build

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.13

RUN apt-get update && apt-get install --no-install-recommends -y build-essential

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /app/venv

COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt > requirements.txt 
RUN /app/venv/bin/pip install -r requirements.txt

COPY . .
RUN poetry build && /app/venv/bin/pip install dist/*.whl

FROM base as final

EXPOSE 9000
COPY --from=build /app/venv /app/venv
COPY .ssh /keys

ENV KEY_DIR="/keys/"

CMD . /app/venv/bin/activate && run-service