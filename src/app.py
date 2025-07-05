from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/math')
def math():
    return render_template('math.html')


if __name__ == '__main__':
    app.run()

