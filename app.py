import sqlite3
from flask import Flask, session, render_template, request, g 

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY, content TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM entries')
    entries = c.fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_enry():
    content = request.form['content']
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    
    c.execute('INSERT INTO entries (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ =='__main__':
    init_db()
    app.run(debug=True)