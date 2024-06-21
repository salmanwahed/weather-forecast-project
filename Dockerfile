FROM python:3.8-bullseye

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY . /app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY weather_forecast/sample.env /app/weather_forecast/.env