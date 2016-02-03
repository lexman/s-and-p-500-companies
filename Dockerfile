# This is a comment
FROM ubuntu:15.04
MAINTAINER Lexman <sisyphus@lexman.org>
RUN apt-get update && apt-get install -y python python-virtualenv python-pip python-psycopg2 postgresql-client
RUN pip install https://github.com/lexman/tuttle/archive/v0.3-rc1.zip
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
VOLUME ["/project"]
WORKDIR /project
