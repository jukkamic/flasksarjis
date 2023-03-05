FROM python:3.8

WORKDIR /appplication

COPY requirements.txt .

RUN pip install -r requirements.txt
# RUN apt update
# RUN apt install mariadb-server -y
RUN pip install application
# RUN pip install gunicorn

COPY application application

#ENV FLASK_APP=application/hello-flask.py
#ENV FLASK_DEBUG=false

EXPOSE 80

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "application:app"]
