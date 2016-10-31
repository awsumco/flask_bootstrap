import os
basedir = os.path.abspath(os.path.dirname(__file__))

DB = ""
DB_USER = ""
DB_PASS = ""
DB_HOSTNAME = ""

# Connect string for  mysql server
#DB_CONN = "mysql+pymysql://%s:%s@%s/%s" % (DB_USER,DB_PASS,DB_HOSTNAME,DB)

# Connect string to sqlite database
DB_CONN = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_DATABASE_URI = DB_CONN
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = 'CHANGE ME'
