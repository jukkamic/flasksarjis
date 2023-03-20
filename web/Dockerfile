FROM nginx:1.23.3

# By default WEB_PATH is empty because build runs in same directory
# docker-compose.yml sets the path relative to the project root
ARG WEB_PATH

COPY ${WEB_PATH}/nginx-default.conf /etc/nginx/conf.d/default.conf
COPY ${WEB_PATH}/buildspec.yml .
