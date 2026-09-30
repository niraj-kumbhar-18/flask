# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/student

from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/student")
def student():
    name = "Rahul"
    rollno = 101
    course = "B.Sc. Computer Science"
    return render_template("student.html", name=name, rollno=rollno, course=course)
 
if __name__ == "__main__":
    app.run(debug=True)
