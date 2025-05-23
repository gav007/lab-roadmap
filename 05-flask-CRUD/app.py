import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DB_NAME = "app.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with open("schema.sql") as f:
        conn = get_db_connection()
        conn.executescript(f.read())
        conn.commit()
        conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    feedbacks = conn.execute('SELECT * FROM feedback ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', feedbacks=feedbacks)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        conn = get_db_connection()
        conn.execute('INSERT INTO feedback (name, message) VALUES (?, ?)', (name, message))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
