FROM python:3.9.0b1-buster
MAINTAINER Almabud
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt
RUN mkdir /app
RUN useradd -ms /bin/bash almabud
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN chown -R almabud:almabud /vol/
RUN chmod -R 755 /vol/web
USER almabud
WORKDIR /app
COPY ./app /app