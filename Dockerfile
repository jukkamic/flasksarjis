FROM twobulls/gunicorn-bootstrap

WORKDIR /appplication

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application application

EXPOSE 80

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "application.app:create_app()"]
