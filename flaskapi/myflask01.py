#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
slappy = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@slappy.route("/hello")
def hello_world():
   return "Hello World"
slappy.add_url_rule("/hello", "hello", hello_world)

if __name__ == "__main__":
   slappy.run(host="0.0.0.0", port=2224) # runs the application
   # slappy.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

