from . import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/hw1')
def hw1():
	return render_template('hw1.html')

@app.route('/hw2')
def h2():
	return render_template('hw2.html')