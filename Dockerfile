FROM ubuntu:latest

MAINTAINER Qpair

RUN apt-get update -y

RUN apt-get install -y python-pip python-dev build-essential

RUN pip install flask-api

RUN pip install ast

RUN pip install flask_pymongo

RUN pip install pymongo

RUN pip install flask_prometheus

WORKDIR /home/ubuntu/flaskapp

COPY . /home/ubuntu/flaskapp

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
