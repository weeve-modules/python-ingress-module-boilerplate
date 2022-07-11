FROM python:3.8-slim

# copy docker-entrypoint and requirements to initialize multi-stage build
COPY ./docker/docker-entrypoint.sh ./requirements.txt /app/

#update the base image before install aditional tools
RUN apt-get update

#install make and others build tools
RUN apt-get install make libglib2.0-dev build-essential -y

# implement multi-stage build to leverage build cache (does not re-install packages when code changes)
RUN pip install -r /app/requirements.txt

# copy source code
COPY ./src /app/src

ENTRYPOINT ["/app/docker-entrypoint.sh"]

# expose docker container port 80 according to weeve spec
EXPOSE 80