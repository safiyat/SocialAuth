__author__ = 'safiyat@zopper.com'

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

import gp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fblogin')
def fb():
    return 'FB'
    pass


@app.route('/gplogin')
def gp_login():
    return redirect(gp.login())

@app.route('/gapicallback')
def gp_redir():
    return gp.check_login(request)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
