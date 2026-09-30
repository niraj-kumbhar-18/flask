# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/courses

from flask import Flask, render_template
app = Flask(__name__)
 
courses = ["Python", "Java", "C Programming", "Web Development", "Data Science"]
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/courses")
def courses_page():
    return render_template("courses.html", courses=courses)
 
if __name__ == "__main__":
    app.run(debug=True)
