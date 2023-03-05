#!/bin/bash
export FLASK_APP=application/hello-flask.py
python -m flask run --host=localhost --port=80
