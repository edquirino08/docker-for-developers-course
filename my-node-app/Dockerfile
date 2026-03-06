FROM node:latest

WORKDIR /app

RUN apt-get update -y && apt-get install -y openssl

COPY package.json /app

RUN npm install

COPY . /app

EXPOSE 3000
CMD [ "node", "index.js" ]