FROM sisyphus:base
MAINTAINER Lexman <sisyphus@lexman.org>
# Specific for SP500 :
RUN apt-get update && apt-get install -y git &&  git config --global user.email "tuttle-bot@lexman.org" && git config --global user.name "Bot"
ADD requirements.txt /root
RUN pip install -r /root/requirements.txt
