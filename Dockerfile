FROM python:latest

WORKDIR /appplication

COPY requirements.txt .

#RUN apt-get update
##RUN pip install --user --no-cache-dir --upgrade pip
#RUN pip install --upgrade pip setuptools wheel
#RUN apt install wget
#RUN wget https://r.mariadb.com/downloads/mariadb_repo_setup
#RUN echo "ad125f01bada12a1ba2f9986a21c59d2cccbe8d584e7f55079ecbeb7f43a4da4  mariadb_repo_setup" | sha256sum -c -
#RUN chmod +x mariadb_repo_setup
#RUN ./mariadb_repo_setup --mariadb-server-version="mariadb-10.6"
#RUN apt-get install libmariadb3 libmariadb-dev -y

RUN pip install -r requirements.txt
#RUN pip install mysql-python
#RUN pip install mariadb
RUN pip install gunicorn

COPY application application

EXPOSE 8000

ENTRYPOINT ["gunicorn"]
CMD ["-w", "3", "-b", "0.0.0.0:8000", "application.app:create_app()"]
