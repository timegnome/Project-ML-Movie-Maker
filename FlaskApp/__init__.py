"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__,template_folder='templates')

import FlaskApp.views