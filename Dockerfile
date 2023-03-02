FROM python:3.8-alpine

WORKDIR /appplication

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application application

ENV FLASK_APP=application/hello-flask.py
ENV FLASK_DEBUG=false

EXPOSE 80

CMD ["xpython3", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]
