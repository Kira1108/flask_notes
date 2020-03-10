from flask import Flask
app = Flask(__name__)
print('Value of __name__ variable: {}'.format(__name__))
print(__name__)
from app import routes
