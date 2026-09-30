# How to Run : 
# Run: python app.py
# http://127.0.0.1:5000/ , http://127.0.0.1:5000/about , http://127.0.0.1:5000/contact

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def home():
    return "<h1>Home Page</h1><p>Welcome to Flask Application.</p>"
 
@app.route('/about')
def about():
    return "<h1>About Us</h1><p>This application is developed using Flask.</p>"
 
@app.route('/contact')
def contact():
    return "<h1>Contact Us</h1><p>Email: info@example.com</p>"
 
if __name__ == "__main__":
    app.run(debug=True)
