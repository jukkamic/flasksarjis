# SARJIS WITH FLASK

**Prerequisites**

Have Python installed and your virtualenv activated

*Visual Studio Code:* **Ctrl + Shift + P** and type *python select interpreter* to select your virtualenv interpreter.

For AWS deployment you will need to install AWS Cli.

**Install and run localhost**
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

**Docker and AWS**

Deploy commands can be found at *AWS Elastic Container Registry - Repositories - Images - View Push Commands* 

Authenticate with AWS:
```bash
aws ecr get-login-password | docker login --username AWS --password-stdin 634129605042.dkr.ecr.eu-west-1.amazonaws.com
```

Build, tag and push to AWS:

```bash
docker build -t ecr-sarjis-repo .

docker tag ecr-sarjis-repo:latest 634129605042.dkr.ecr.eu-west-1.amazonaws.com/ecr-sarjis-repo:latest

docker push 634129605042.dkr.ecr.eu-west-1.amazonaws.com/ecr-sarjis-repo:latest
```

**TIPS**

```bash
aws ecs update-service --cluster MyDockerCluster --service MyDockerEcsService2 --force-new-deployment
```

```bash
pip install pip-check-reqs
```

