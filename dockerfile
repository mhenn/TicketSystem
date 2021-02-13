FROM python:latest


RUN pip install cryptography flask flask-cors flask-jwt-extended flask-restx mock mockupdb mongomock pymongo pytest pytest-dependency pytest-mock python-keycloak

