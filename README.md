# flask_bootstrap
Flask Bootstrap, You know to start a new Flask app

# Getting started with your first Flask app.

* Download this repo to your PC
```bash
 wget https://github.com/awsumco/flask_bootstrap/archive/master.zip 
```
* Extract and move master directory to new flask project name
```bash
unzip master.zip
mv flask_bootstrap-master/ new_project_name
```
* Setup new python virtual environment and install flask dependencies
```bash
virtualenv-2.7 venv
. ./venv/bin/activate
pip install -r requirements.txt
```
* Copy config_example.py to config.py, edit as needs be.
* Create your new SQL db
```bash
./db_create.py
```   
* Test the initial app and fix errors.
```
./run.py
```
