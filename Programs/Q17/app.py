# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/temperature

from flask import Flask, render_template, request
app = Flask(__name__)
 
@app.route('/temperature', methods=['GET', 'POST'])
def temperature():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        conversion = request.form['conversion']
 
        if conversion == 'CtoF':
            result = (value * 9 / 5) + 32
        else:
            result = (value - 32) * 5 / 9
 
    return render_template('temperature.html', result=result)
 
if __name__ == "__main__":
    app.run(debug=True)
