# SARJIS WITH FLASK

**Prerequisites**

Have Python installed and your virtualenv activated

*Visual Studio Code:* **Ctrl + Shift + P** and type *python select interpreter* to select your virtualenv interpreter.

**Install**
```bash
pip install -r requirements.txt
```

set the environment variable
```bash
export FLASK_APP=hello-flask.py
# In Windows PowerShell use
$env:FLASK_APP="application/hello-flask.py"
```

and run
```bash
python -m flask run
```

(Optional: Set the environment variable FLASK_ENV for development or production environment)


