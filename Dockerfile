FROM python:latest

RUN apt-get update -y && apt-get upgrade -y

RUN pip3 install -U pip

RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /app/
WORKDIR /app/
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

CMD bash start
