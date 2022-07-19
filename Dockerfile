FROM python:3.9.13-slim

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt


RUN mkdir -p /src
COPY . /src/

WORKDIR /src
CMD gunicorn --bind :8000 --reload user_app.wsgi
