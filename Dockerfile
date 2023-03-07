FROM python:3.8

WORKDIR /appplication

COPY requirements.txt .

#RUN python -m pip install --upgrade pip
#RUN pip install wheel
RUN pip install -r requirements.txt
# RUN pip install psycopg2
#RUN apt-get update
#RUN apt-get install libmariadbclient-dev
RUN pip install application
#RUN cores=$(nproc --all)
#RUN workers=$((cores * 2 + 1))
#ENV WORK=${workers}

RUN pip install gunicorn

COPY application application

# ENV FLASK_APP=application/app.py
# ENV FLASK_DEBUG=False

EXPOSE 80

#CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "application.app:create_app()"]
ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:80", "application.app:create_app()"]
