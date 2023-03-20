FROM postgres:alpine3.17

# By default DB_PATH is empty because build runs in same directory
# docker-compose.yml sets the path relative to the project root
ARG DB_PATH
ARG postgres_password

WORKDIR /application

ENV POSTGRES_PASSWORD=${postgres_password}

EXPOSE 5432:5432

COPY ${DB_PATH}/buildspec.yml .
