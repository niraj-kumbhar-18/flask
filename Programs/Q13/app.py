# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/contact

from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "flasklab"
 
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
 
        if name == "" or email == "" or subject == "" or message == "":
            flash("All fields are required!")
        else:
            flash("Message Sent Successfully!")
 
    return render_template('contact.html')
 
if __name__ == "__main__":
    app.run(debug=True)
