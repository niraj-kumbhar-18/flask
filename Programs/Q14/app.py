# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/event

from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "flasklab"
 
@app.route('/event', methods=['GET', 'POST'])
def event():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        event_name = request.form['event_name']
 
        if name == "" or mobile == "":
            flash("Name and Mobile Number are required!")
        else:
            flash(f"Registered Successfully! Name: {name}, Mobile: {mobile}, Event: {event_name}")
 
    return render_template('event.html')
 
if __name__ == "__main__":
    app.run(debug=True)
