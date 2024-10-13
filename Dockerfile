# Pull base image
FROM python:3.10.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
# RUN pip install -U pip \
#     && apt-get update \
#     && apt install -y curl netcat \
#     && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# ENV PATH="${PATH}:/root/.poetry/bin"

# Copy project
COPY . /app/

# RUN poetry config virtualenvs.create false \
#   && poetry install --no-interaction --no-ansi

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

