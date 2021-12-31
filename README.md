# Test API

This is a test API using the Python Flask framework. It is
essentially a wrapper around the API at https://bpdts-test-app.herokuapp.com/
which allows querying for people who either live in a city or are
currently a certain distance from the centre of that city.

To this end, it provides a single endpoint:

    /v1/users_in_or_near/<city>/<unit>/<distance>

This endpoint returns a JSON list of people who match the criteria of
either:

1. Live in the given city
1. Are currently less than the specified distance from the city

They are indexed by the ID of the person, so do not contain duplicates 
where a person matches both criteria.

The code was specifically written to a specification asking for people
currently living in London or whose coordinates are within 50 miles
of London. Thus the current endpoint is guaranteed to work:

    /v1/users_in_or_near/London/miles/50

In principle, others will work, but are dependent on data being available
in the source API and city locations being present in *app/constants.py*.

## Installation

Check the code out from github into a directory.

Optional but recommended: create a Python virtual environment and 
activate it

    $ python -m venv venv
    $ source venv/bin/activate
    (venv) $

Install the requirements (you only need to install gunicorn if you're 
going to use it to run Flask in production):

    (venv) $ pip install -r requirements/dev.txt -r requirements/prod.txt
    (venv) $ pip install gunicorn

Set the Flask app environment variable:

    (venv) $ export FLASK_APP=main.py

## Running the Flask app

You can run the app in various ways:

You can run the unit tests:

    (venv) $ flask test

You can run the development server, after which the API will respond on
http://localhost:5000/v1/users_in_or_near/London/miles/50

    (venv) $ export FLASK_DEBUG=1
    (venv) $ flask run

You can run a production server using gunicorn (or any other HTTP server/proxy of choice). Note:
the 'flask deploy' step here is currently a no-op, but it's good practice to get into the
habit of using it when deploying a Flask app to production. The app will respond on the same URL 
as before, although you can obviously change that in the gunicorn config.

    (venv) $ export FLASK_DEBUG=0
    (venv) $ flask deploy
    (venv) $ gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - main:app

## Deploy from Docker

If you don't want to install the code, or Flask, you can deploy from
a Docker container hosted on my Docker hub. This command will start a 
server on port 5000, but the Docker command can be edited to change that.

    $ docker container run --name 156379 -d -p 8000:5000 djm4/156379:latest

If have cloned the git repo, you can build your own Docker image from it using:

    $ docker image build -t 156379:latest .

## Links

* Python Flask framework https://flask.palletsprojects.com/en/2.0.x/