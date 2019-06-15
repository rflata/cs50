from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

students = []


@app.route("/")
def index():
    #name = request.args.get("name", "world")
    return render_template("index.html")


@app.route("/registered")
def registered():
    with open("registered.csv", "r") as reg:
        reader = csv.reader(reg)
        students = list(reader)
    return render_template("registered.html", students=students)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    with open('registered.csv', 'a') as registered:
        writer = csv.writer(registered)
        writer.writerow((name, dorm))
    students.append(name + " from " + dorm)
    return render_template("success.html")
