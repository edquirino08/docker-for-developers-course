FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install Flask requests

COPY . .

EXPOSE 5000

CMD [ "python", "./app.py" ]