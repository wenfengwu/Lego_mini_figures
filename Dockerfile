FROM python:3.8-bullseye

RUN apt-get update -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

# Install packages. Flask, Mysql Client, Bcrypt and etc
RUN pip install -r requirements.txt

# Start up command
ENTRYPOINT [ "python" ]

# Start up arguments
CMD [ "app.py" ]