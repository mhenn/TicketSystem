FROM ubuntu:20.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 python3-pip -y
RUN apt-get update
RUN apt-get install libcppunit-dev -y
RUN pip3 install python-keycloak requests  Flask flask-restx Flask-Cors flask-jwt-extended cryptography mock mongomock mockupdb pymongo pytest pytest-dependency pyOpenSSL 

COPY packages /packages

WORKDIR /packages/decorators/
RUN pip3 install -e .
WORKDIR /packages/token_connect/
RUN pip3 install -e .
WORKDIR /packages/flask_setup/
RUN pip3 install -e .

WORKDIR /
COPY loop.sh loop.sh
RUN chmod +x loop.sh
ENTRYPOINT ./loop.sh && /bin.bash
