from flask import Flask, render_template, request

app = Flask(__name__)

f = open("cpu_usage.txt", "w")
f.write(str(0.0))
f.close()

@app.route("/")
def home():
    f = open("cpu_usage.txt", "r")
    cpu_usage = float(f.read())
    f.close()
    if cpu_usage <= 3:
        return render_template("index1.html")
    else:
        return render_template("index2.html")


app.run(debug=True, port=4000)
