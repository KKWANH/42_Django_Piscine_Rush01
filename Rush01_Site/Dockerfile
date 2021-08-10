FROM	python:3.9

RUN		mkdir /code
WORKDIR	/code
COPY	. /code
RUN		python3 -m pip install --upgrade pip
RUN		pip install -r requirement.txt
RUN		python3 /code/manage.py makemigrations
RUN		python3 /code/manage.py migrate