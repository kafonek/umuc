from . import app
from flask import render_template, request
from flask_wtf import Form
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import Required, ValidationError

@app.route('/')
def index():
	return render_template('index.html')

### TODO: move these into their own forms.py file
class HW1(Form):
	integer1 = IntegerField(label="First integer", validators=[Required()])
	integer2 = IntegerField(label="Second integer", validators=[Required()])
	operation = SelectField(label="Operation",  
			                choices=[('+', 'addition'), ('-', 'subtraction'), ('*', 'multiplication'),
			                		 ('/', 'division'), ('%', 'modulus'), ('&', 'bitwise and'),
			                		 ('|', 'bitwise or')])
	submit = SubmitField('Submit')


@app.route('/hw1', methods=['GET', 'POST'])
def hw1():
	form = HW1()
	output = None
	if form.validate_on_submit():
		int1 = form.data['integer1']
		int2 = form.data['integer2']
		operation = form.data['operation']
		# normally eval isn't safe, but we're using sanitized input
		result = eval('%s %s %s' % (int1, operation, int2)) 
		output = "The result of %s %s %s is %s" % (int1, operation, int2, result)

	return render_template('hw1.html', form=form, output=output)

@app.route('/hw2')
def h2():
	return render_template('hw2.html')
