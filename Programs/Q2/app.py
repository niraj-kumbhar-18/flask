# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/student/101/Rahul


from flask import Flask
app = Flask(__name__)
 
@app.route('/student/<int:roll_no>/<name>')
def student(roll_no, name):
    return f"""
    <h1>Student Details</h1>
    <b>Roll Number:</b> {roll_no}<br>
    <b>Name:</b> {name}
    """
 
if __name__ == "__main__":
    app.run(debug=True)
