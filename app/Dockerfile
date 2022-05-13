# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /code/app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .
