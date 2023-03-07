#!/bin/bash
export FLASK_APP=../application/app.py
export FLASK_DEBUG=True
python -m flask run --host=localhost --port=80

