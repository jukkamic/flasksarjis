FROM python:3.8-slim-buster

WORKDIR /appplication

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application application

ENV FLASK_APP=application/hello-flask.py
ENV FLASK_DEBUG=false

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["./application/hello-flask.py"]
