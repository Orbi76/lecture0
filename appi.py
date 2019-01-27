import datetime

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/note", methods=["GET", "POST"])
def uzi():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("name")
        session["notes"].append(note)
    return render_template("index.html", notes=session["notes"])


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
    return render_template("udv.html", name=name)


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


@app.route("/video")
def video():
    return render_template("video.html")


if __name__ == '__main__':
    app.run(debug=True)
# export FLASK_APP=appi.py kivalasztom melyiket inditsa a flask.
# export FLASK_ENV=development  ilyenkor nem kell mindig ujrainditani a szervert
# flask run  igy inditon el a szervert
# pip parancsal installalok programot
