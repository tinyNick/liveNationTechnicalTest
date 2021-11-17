FROM python:3.7.3-alpine3.9

EXPOSE 5000
ENV PYTHONDONTWRITEBYTECODE=1
ENV FLASK_APP=server.py
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app
COPY ./src/requirements.txt /app/requirements.txt
RUN python -m pip install -r requirements.txt
COPY ./src /app

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
