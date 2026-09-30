# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/age

from flask import Flask, render_template, request, flash
from datetime import date, datetime
app = Flask(__name__)
app.secret_key = "flasklab"
 
@app.route('/age', methods=['GET', 'POST'])
def age():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
 
        if name == "" or dob == "":
            flash("Name and Date of Birth are required!")
        else:
            birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
            today = date.today()
            age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            flash(f"Name: {name}, Age: {age_years} years")
 
    return render_template('age.html')
 
if __name__ == "__main__":
    app.run(debug=True)
