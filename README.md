# SARJIS WITH FLASK

**TODO**

- There is no dev or prod environments. The configuration is hardcoded into app.py (DevelopmentConfig)
- docker-compose build does not work. Build scripts must be run individually for each container
- Some comics get caught up in some errors
- Set your specific AWS and Azure configurations in (env) config

**Prerequisites**

Have Python installed and your virtualenv activated

*Visual Studio Code:* **Ctrl + Shift + P** and type *python select interpreter* to select your virtualenv interpreter.

For AWS deployment you will need to install AWS Cli.

## Install and run localhost

```bash
pip install -r requirements.txt
```

set the environment variable
```bash
export FLASK_APP=application/app.py
# In Windows PowerShell use
$env:FLASK_APP="application/app.py"
```
and run
```bash
python -m flask run --host=localhost --port=8000
```

(Optional: Set the environment variable FLASK_ENV for development or production environment)

## Docker in localhost

Build the UI

```bash
ng build --configuration development
```

Run the **build.sh** scripts in **db/** and **web/** and run **build-service.sh** in project root.

Run **docker-compose up** in project root.

http://localhost/

## Docker with AWS or Azure

**AWS**

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

**Azure**

All *build.sh* and *push.sh* scripts work with *az* parameter to build and deploy to Azure.

**TIPS**

```bash
aws ecs update-service --cluster MyDockerCluster --service MyDockerEcsService2 --force-new-deployment
```

```bash
pip install pip-check-reqs
```

