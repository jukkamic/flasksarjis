FROM python:3.8-alpine

WORKDIR /appplication

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application application

ENV FLASK_APP=application/hello-flask.py
ENV FLASK_ENV=development

EXPOSE 80

CMD ["flask", "run", "--port=80"]
