# Sample Store

This app uses Django Rest Framework to expose an API for managing a collection of data about samples from subjects that participate in a research project. 

## Installation and Launching

1. Clone the repository
2. Get a local_settings.py file and docker-compose.override.yml file from someone on the team
3. cd to the top-level samplestore directory
4. Create a virtualenv and enter it
5. Install pip packages 'pip install -r app/requirements.txt'
6. Make migrations 'python app/manage.py makemigrations' and apply them 'python app/manage.py migrate'
7. Run 'docker-compose build'
8. Run 'docker-compose up'
9. Go to http://0.0.0.0:8000

## Authentication

Sample Store uses DBMI's own py-auth0-jwt-rest pypi package to authenticate requests. This package expects that incoming requests to the Sample Store have an "Authorization" request header with a value of "JWT [jwt encoded string]". The package allows for this application to accept requests from multiple different Auth0 Client IDs within the greater HMS DBMI Auth0 account.

## Permissions

Object level permissions will be stored in DBMI's SciAuthZ microservice.