# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def salary():
    emp_id = 1001
    name = "Amit Kumar"
    department = "IT"
    basic_salary = 50000
 
    hra = basic_salary * 0.20
    da = basic_salary * 0.12
    ta = basic_salary * 0.08
    pf = basic_salary * 0.10
 
    gross_salary = basic_salary + hra + da + ta
    net_salary = gross_salary - pf
 
    return f"""
    <h1>Employee Salary Slip</h1>
    <b>Employee ID:</b> {emp_id}<br>
    <b>Name:</b> {name}<br>
    <b>Department:</b> {department}<br>
    <b>Basic Salary:</b> {basic_salary}<br>
    <b>HRA (20%):</b> {hra}<br>
    <b>DA (12%):</b> {da}<br>
    <b>TA (8%):</b> {ta}<br>
    <b>PF (10%):</b> {pf}<br>
    <b>Gross Salary:</b> {gross_salary}<br>
    <b>Net Salary:</b> {net_salary}
    """
 
if __name__ == "__main__":
    app.run(debug=True)
