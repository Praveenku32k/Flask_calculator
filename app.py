from flask import Flask
from flask import request
from flask import render_template



app=Flask(__name__)

@app.route("/") # creating the url home route.

def welcome():
    return "hello! this is first project for you!!!!!....."

if __name__=='__main__':
    app.run(port=8000)





