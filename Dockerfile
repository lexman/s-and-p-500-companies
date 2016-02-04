# Main sisyphus needs
FROM debian:jessie
MAINTAINER Lexman <sisyphus@lexman.org>
RUN apt-get update && apt-get install -y python python-psycopg2 postgresql-client python-pip 
RUN pip install --upgrade pip
RUN pip install https://github.com/lexman/tuttle/archive/v0.3-rc1.zip
VOLUME ["/project"]
WORKDIR /project

# Specific for SP500 :
RUN apt-get update && apt-get install -y git
ADD requirements.txt /root
RUN pip install -r /root/requirements.txt
