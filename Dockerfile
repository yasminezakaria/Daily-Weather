# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /Daily-Weather

# add the current directory to the container as /app
ADD . /Daily-Weather

# execute everyone's favorite pip command, pip install -r
RUN pip install --upgrade --trusted-host pypi.python.org -r requirements.txt

# execute the Flask app

EXPOSE 5000

CMD ["python", "Server.py"]
