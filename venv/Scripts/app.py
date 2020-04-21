
from flask import Flask, request
from Movies import movieMetadata

app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  

@app.route('/api/movie/<string:name>') 
def api(name):
   merged=movieMetadata(name)
   return merged

@app.route('/api/movie/') 
def search():
    search_value= request.args.get('search_field')
    
    return '<h1> it is {}</h1>'.format(search_value)
