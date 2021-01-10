
from flask import Flask, request, render_template 
from flask_cors import CORS, cross_origin
import logging
import datetime
import sys
import os
import subprocess
app = Flask(__name__)


@cross_origin()  # allow all origins all methods.
@app.route('/')
def content():
    with open("output.txt", "w+") as output:
        subprocess.call(['python3', './print.py'], stdout=output)
    with open('output.txt', 'r') as f:
        return render_template('content.html', text=f.read())


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
