FROM postgres:16

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5433

VOLUME [ "/backup/" ]