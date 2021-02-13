FROM ubuntu:20.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip -y

RUN pip3 install python-keycloak requests flask_restx Flask Flask-Cors flask-jwt-extended cryptography mock mongomock mockupdb pymongo pytest pytest-dependency 

COPY loop.sh loop.sh
RUN chmod +x loop.sh
ENTRYPOINT ./loop.sh && /bin.bash
