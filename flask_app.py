
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Meme World!, Dabbin on the haters'

@app.route('/nana')
def nan():
    return 'I\'m a bonana'

@app.route('/home')
def rend_home():
    return render_template('index.html')
