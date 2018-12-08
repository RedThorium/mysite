
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from data import MyData

app = Flask(__name__)

theData = MyData()

@app.route('/')
def hello_world():
    return 'Hello from Meme World!, Dabbin on the haters'

@app.route('/nana')
def nan():
    return 'I\'m a bonana'

@app.route('/home')
def rend_home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    return render_template('data.html', mydata = theData)

if __name__ == '__main__':
    app.run(debug=True)
