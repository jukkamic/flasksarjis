FROM postgres:alpine3.17

WORKDIR /application

ARG postgres_password
ENV POSTGRES_PASSWORD=${postgres_password}

EXPOSE 5432:5432

COPY buildspec.yml .
