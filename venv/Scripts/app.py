
from flask import Flask
from connection import movieMetadata

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  


@app.route('/hello/movieMetadata/<string:name>')
def hello(name):
    ab=movieMetadata(name)
    return ab

