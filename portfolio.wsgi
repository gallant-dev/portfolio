#!/usr/bin/python
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def showPortfolio():
    return render_template('index.html')

if __name__ == '__main__':
    application.secret_key = 'FiA;\\BJ\xa0\xad\xe5\xd8\xff\xa5\xfc\xd8v'
    application.debug = True
    application.run(host='0.0.0.0', port=8000)
