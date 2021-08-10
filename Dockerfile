From python:3.7

RUN mkdir /usr/src/app
RUN mkdir /usr/src/static
WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirement.txt .
RUN python -m pip install --upgrade -r requirement.txt

COPY . .
