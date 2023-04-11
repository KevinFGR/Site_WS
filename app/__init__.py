from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__, static_folder="static")

app.config.from_object("config.py")

mysql=MySQL(app)