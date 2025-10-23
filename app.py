
from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "Success is not in what you have, but who you are.",
    "Dream bigger. Do bigger.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Don’t stop when you’re tired. Stop when you’re done."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def quote():
    return render_template('quote.html', quote=random.choice(quotes))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
