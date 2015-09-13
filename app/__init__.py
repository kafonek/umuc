from flask import Flask
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
# Adding a SECRET_KEY is necessary to use forms with CSRF protection
app.config['SECRET_KEY'] = 'umuc test project'


from . import views