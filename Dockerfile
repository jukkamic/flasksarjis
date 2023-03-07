FROM python:3.8

WORKDIR /appplication

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install application
RUN pip install gunicorn

COPY application application

EXPOSE 80

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:80", "application.app:create_app()"]
