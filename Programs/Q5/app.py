# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/employees

from flask import Flask, render_template
app = Flask(__name__)
 
employees = [
    {"name": "Rahul", "department": "IT", "experience": 1},
    {"name": "Priya", "department": "HR", "experience": 4},
    {"name": "Amit", "department": "Sales", "experience": 8}
]
 
@app.route("/")
def home():
    return render_template("home.html")
 
@app.route("/employees")
def employee():
    return render_template("employees.html", employees=employees)
 
@app.route("/department")
def department():
    return render_template("department.html")
 
if __name__ == "__main__":
    app.run(debug=True)
