CREATE DATABASE flaskdocker;

\connect flaskdocker;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);