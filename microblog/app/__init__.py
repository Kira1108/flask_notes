from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# print('Value of __name__ variable: {}'.format(__name__))
from app import routes
