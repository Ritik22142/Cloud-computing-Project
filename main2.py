from flask import Flask, render_template, request

app = Flask(__name__)
count = 0


@app.route("/")
def home():
    if count > 1:
        return render_template("index.html")
    else:
        return render_template("index2.html")


@app.route("/index2")
def index2():
    global count
    count += 1
    print(count)
    return render_template("index2.html")


app.run(debug=True, port=8000)
