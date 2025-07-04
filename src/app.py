from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello, Rebekah!</h1><p>I made this.</p>'


if __name__ == '__main__':
    app.run()

