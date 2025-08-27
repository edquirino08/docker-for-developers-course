FROM python:3

RUN apt-get update -y && \
    apt-get install -y python3-dev

WORKDIR /app

RUN pip install Flask
RUN pip install psycopg2-binary

COPY . .

EXPOSE 5001

CMD [ "python", "./app.py" ]