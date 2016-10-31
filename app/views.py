import pprint, os, imghdr
from datetime import datetime
from flask import render_template, flash, redirect, request
from app import app
from app import db, models
from sqlalchemy import desc, func

from .forms import LoginForm
from .models import User


@app.route('/')
def index():
  return render_template("index.html")
  


