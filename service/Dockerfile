FROM twobulls/gunicorn-bootstrap

# By default SERVICE_PATH is set because build is run from project root
ARG SERVICE_PATH=service

COPY ${SERVICE_PATH}/buildspec.yml /buildspec.yml

WORKDIR /application

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application application

EXPOSE 8000:8000

ENTRYPOINT ["gunicorn"]
CMD ["-w", "3", "-b", "0.0.0.0:8000", "application.app:create_app()"]
