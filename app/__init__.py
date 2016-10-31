import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
from flask_moment import Moment


csrf = CsrfProtect()
app = Flask(__name__)
app.config.from_object('config')
csrf.init_app(app)
db = SQLAlchemy(app)

app.config.from_object('config')
moment = Moment(app)


from app import views, models

# Jinja Globals Example
# app.jinja_env.globals.update(JINJAVAR=PYTHON_THINGY)
