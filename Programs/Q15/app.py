# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/electricity

from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "flasklab"
 
@app.route('/electricity', methods=['GET', 'POST'])
def electricity():
    if request.method == 'POST':
        name = request.form['name']
        consumer_no = request.form['consumer_no']
        units = request.form['units']
 
        if name == "" or consumer_no == "" or units == "":
            flash("All fields are required!")
        else:
            units = int(units)
            if units <= 100:
                bill = units * 3
            elif units <= 200:
                bill = (100 * 3) + (units - 100) * 5
            else:
                bill = (100 * 3) + (100 * 5) + (units - 200) * 7
 
            flash(f"Consumer: {name}, Units: {units}, Total Bill: Rs.{bill}")
 
    return render_template('electricity.html')
 
if __name__ == "__main__":
    app.run(debug=True)
