# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/result

from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/result")
def result():
    name = "Rahul"
    percentage = 65
    return render_template("result.html", name=name, percentage=percentage)
 
if __name__ == "__main__":
    app.run(debug=True)
