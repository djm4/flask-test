FROM python:3.6-alpine

# Set up environment variables
ENV FLASK_APP main.py
ENV FLASK_CONFIG docker

# Set up a user so we don't run as root
RUN adduser -D flask
USER flask

WORKDIR /home/flask

# Set up Python environment and copy in required files
COPY requirements requirements
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY main.py config.py boot.sh ./

# runtime configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]