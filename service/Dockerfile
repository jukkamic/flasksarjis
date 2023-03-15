FROM twobulls/gunicorn-bootstrap

WORKDIR /appplication

COPY requirements.txt .
COPY service/buildspec.yml .

RUN pip install -r requirements.txt

COPY application application
COPY service/buildspec.yml .

EXPOSE 8000:8000

ENTRYPOINT ["gunicorn"]
CMD ["-w", "3", "-b", "0.0.0.0:8000", "application.app:create_app()"]
