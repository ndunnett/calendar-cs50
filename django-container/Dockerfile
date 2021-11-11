FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /source
COPY ./source /source
WORKDIR /source/core

RUN adduser --disabled-password --gecos '' dockeruser
USER dockeruser