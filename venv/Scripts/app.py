
from flask import Flask
from connection import movieMetadata

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  


@app.route('/api/movie/<string:name>', methods=['GET', 'POST']) 
def api(name):
    merged=movieMetadata(name)
    return merged

