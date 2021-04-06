FROM python:3.9.1

RUN apt-get update && apt-get install -y gettext libxmlsec1-dev xmlsec1 && \
    pip install --upgrade pip poetry

WORKDIR /app

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false && poetry install

COPY . /app

RUN ["chmod", "a+x", "/app/entry"]

ENTRYPOINT ["/app/entry"]
CMD ["runserver"]
