# flask_bootstrap
Flask Bootstrap, You know to start a new Flask app

# Getting started with your first Flask app.

1. Download this repo to your PC
```bash
 wget https://github.com/awsumco/flask_bootstrap/archive/master.zip 
```

2. Extract and move master directory to new flask project name
```bash
unzip master.zip
mv flask_bootstrap-master/ new_project_name
```

3.Setup new python virtual environment and install flask dependencies
```bash
virtualenv-2.7 venv
. ./venv/bin/activate
pip install -r requirements.txt
```

4. Copy config_example.py to config.py, edit as needs be.

5. Create your new SQL db
```bash
./db_create.py
```   

6. Test the initial app and fix errors.
```
./run.py
```
