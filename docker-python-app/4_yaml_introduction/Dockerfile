FROM python:3


RUN apt-get update -y && \
    apt-get install -y python3-dev

WORKDIR /app

RUN pip install PyYAML Flask

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD [ "python", "./app.py" ]
