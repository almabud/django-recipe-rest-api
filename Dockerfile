FROM python:3.9.0b1-buster
MAINTAINER Almabud
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt && mkdir /app && useradd -ms /bin/bash almabud
USER almabud
WORKDIR /app
COPY ./app /app