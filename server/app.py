from flask import Flask
import os
app = Flask(__name__)
app.config['MONGO_IP'] = os.environ.get('MONGO_IP')
app.config['SQL_IP'] = os.environ.get('SQL_IP')
app.config['SECRET_KEY'] = 'yckcmkg'#random secret key for dev purposes