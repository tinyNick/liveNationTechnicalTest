FROM python:3.7.3-alpine3.9

EXPOSE 5000
ENV PYTHONDONTWRITEBYTECODE=1
ENV FLASK_APP=server.py
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

COPY ./src/requirements.txt /app/requirements.txt
RUN python -m pip install -r requirements.txt
RUN python -m pip install uwsgi

COPY ./src /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD uwsgi --http 127.0.0.1:8000 --wsgi-file server.py --callable app
