# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/

from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("home.html")
 
if __name__ == "__main__":
    app.run(debug=True)
