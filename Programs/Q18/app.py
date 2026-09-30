# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/attendance

from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "flasklab"
 
@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        name = request.form['name']
        total_days = request.form['total_days']
        present_days = request.form['present_days']
 
        if name == "" or total_days == "" or present_days == "":
            flash("All fields are required!")
        else:
            total_days = int(total_days)
            present_days = int(present_days)
            percentage = (present_days / total_days) * 100
 
            if percentage >= 75:
                status = "Eligible"
            else:
                status = "Not Eligible"
 
            flash(f"Name: {name}, Attendance: {percentage:.2f}%, Status: {status}")
 
    return render_template('attendance.html')
 
if __name__ == "__main__":
    app.run(debug=True)
