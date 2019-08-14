FROM python:3.7.4-buster
RUN mkdir /client
WORKDIR /client
COPY . /client
ENV PYTHONUNBUFFERED=0
RUN pip install --upgrade pip

RUN apt-get clean && \
apt-get update && \
apt-get install --no-install-recommends -y build-essential apt-transport-https && \
apt-get clean && \
apt-get update

RUN pip install -r /client/requirements.txt