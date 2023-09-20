# pull official base image
FROM python:3.10-alpine3.15


# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1


# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1


# set work directory
WORKDIR /app


# update the system and add git
RUN apk update
RUN apk add git


# install dependencies
COPY ./requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt


# copy project
COPY . /app


# specify the entry point
RUN chmod 755 /app/gunicorn_starter.sh
ENTRYPOINT [ "./gunicorn_starter.sh" ]