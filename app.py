from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def login():  # put application's code here
    return render_template("login.html")


@app.route('/index.html')
def index():  # put application's code here
    i = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    return render_template("index.html", i=i)


if __name__ == '__main__':
    app.run()
