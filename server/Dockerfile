# pull official base image
FROM python:3.9-slim-buster

WORKDIR /usr/src

# set working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get clean \
    && apt install -y git \
    && apt install -y sqlite3 libsqlite3-dev \
    && apt install -y libopenblas-dev build-essential cmake 


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .