# How to run:
# Run: python app.py
# Open in browser: http://127.0.0.1:5000/  (Read - shows all records)
# Click Add New Student to Create a record.
# Click Edit on a row to Update that record.
# Click Delete on a row to Delete that record.

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
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM student').fetchall()
    conn.close()
    return render_template('index.html', students=students)
 
@app.route('/add', methods=['GET', 'POST'])
def add():
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
 
    return render_template('add.html')
 
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM student WHERE id = ?', (id,)).fetchone()
 
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
 
        conn.execute('UPDATE student SET name = ?, age = ?, course = ? WHERE id = ?',
                     (name, age, course, id))
        conn.commit()
        conn.close()
        return redirect('/')
 
    conn.close()
    return render_template('edit.html', student=student)
 
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM student WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')
 
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
