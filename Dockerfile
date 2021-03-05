FROM python:3.7-buster as builder

ENV PYTHONUNBUFFERED 1

COPY pyproject.toml /app/
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends default-libmysqlclient-dev gcc libffi-dev make && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    pip install pex

COPY src /app/src

RUN pex -vvv . -o dist/ckchina-search-$(date +"%Y%m%d%H%M%S").pex --venv prepend --compile -c gunicorn --validate-entry-point \
--use-system-time

FROM python:3.7-slim

RUN mkdir /app && mkdir /app/logs

COPY --from=builder /app/dist/ckchina-search* /app/

COPY resources/* /app/

EXPOSE 8000

WORKDIR /app
