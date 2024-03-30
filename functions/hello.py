# functions/hello.py
from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = '../templates'

@app.route('/.netlify/functions/hello')
def hello():
    return render_template('index.html', name='World')
