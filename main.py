from flask import Flask, render_template, request

app = Flask(__name__)
count = 0


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index2")
def index2():
    global count
    count += 1

    print(count)
    return render_template("index2.html")


app.run(debug=True, port=5000)
