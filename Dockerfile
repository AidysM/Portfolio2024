# Pull base image
FROM python:slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install and setup poetry
RUN pip install -U pip \
    && apt-get update \
    && apt install -y curl netcat \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /app
COPY . /app/
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

