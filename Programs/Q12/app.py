# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/employee

from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route('/employee', methods=['GET', 'POST'])
def employee():
    details = None
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        name = request.form['name']
        department = request.form['department']
        designation = request.form['designation']
        details = {
            "emp_id": emp_id,
            "name": name,
            "department": department,
            "designation": designation
        }
    return render_template('employee_form.html', details=details)
 
if __name__ == "__main__":
    app.run(debug=True)
