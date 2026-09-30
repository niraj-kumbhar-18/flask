# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/  (shows all records)
# Open: http://127.0.0.1:5000/add  (to insert a new record, then it redirects back to home page)

from flask import Flask, render_template, request, redirect
import sqlite3
 
app = Flask(__name__)
 
def get_db_connection():
    conn = sqlite3.connect('student.db')
    conn.row_factory = sqlite3.Row
    return conn
 
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
 
@app.route('/')
def home():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM student').fetchall()
    conn.close()
    return render_template('home.html', students=students)
 
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
 
        conn = get_db_connection()
        conn.execute('INSERT INTO student (name, age, course) VALUES (?, ?, ?)',
                     (name, age, course))
        conn.commit()
        conn.close()
        return redirect('/')
 
    return render_template('add_student.html')
 
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
