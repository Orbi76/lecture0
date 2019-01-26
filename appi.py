import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return "indexhtml kiirja is"


@app.route("/<string:name>")
def helloakarki(name):
    name = name.capitalize()
    return f"Hello, {name}!"


@app.route("/i")
def indexhtml():
    return render_template("index.html")


@app.route("/jinja")
def jin():
    headline = "Amit ide irok az jelenik meg az oldaln Jinja"
    return render_template("jinjapelda.html", headline=headline)


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)


@app.route("/ho")
def ho():
    return "<h1>Remelem ez megy </h1>"


@app.route("/hny")
def hny():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 27
#        new_year = True
    return render_template("hny.html", new_year=new_year)


@app.route("/na")
def na():
    names = ["Juli", "Maci", "Gabor"]
    return render_template("namepage.html", names=names)


@app.route("/vid")
def vid():
    return render_template("juli.html")


if __name__ == '__main__':
    app.run(debug=True)
