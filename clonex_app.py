
from flask import Flask, request
from flask_cors import CORS, cross_origin
import logging, datetime , sys
import os
import subprocess
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@cross_origin() # allow all origins all methods.


@app.route('/headlesstree', methods=['POST']) 
def headlesstree():
    if request.method == 'POST':
        id = request.args.get('id')
        timeout = request.args.get('timeout')
        if not timeout:
            timeout = 30
        subprocess.call(['sh', './scripts/headless.sh', '%s' %id, '%s' %timeout])
    return 'ID is {0}, timeout is {1}'.format(id, timeout)
    

@app.route('/headlesstree', methods=['DELETE']) 
def deleteheadlesstree():
    if request.method == 'DELETE':
        id = request.args.get('id')
        subprocess.call(['sh', './scripts/delete-headless.sh', '%s' %id])
    return 'ID of headlesstree to be deleted is {0}'.format(id)


@app.route('/worktree', methods=['POST']) 
def worktree():
    if request.method == 'POST':
        id = request.args.get('id')
        subprocess.call(['sh', './scripts/worktree.sh', '%s' %id])
    return 'ID of worktree created branch {0}'.format(id)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
