from flask import Flask, render_template, request, jsonify, g
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
DATABASE = 'typing_history.db'

# Database setup
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                wpm INTEGER NOT NULL,
                accuracy INTEGER NOT NULL,
                difficulty TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_result', methods=['POST'])
def save_result():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO history (wpm, accuracy, difficulty) VALUES (?, ?, ?)',
        (data['wpm'], data['accuracy'], data['difficulty'])
    )
    db.commit()
    return jsonify({'status': 'success'})

@app.route('/get_history')
def get_history():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT wpm, accuracy, difficulty, timestamp FROM history ORDER BY timestamp DESC LIMIT 5')
    history = cursor.fetchall()
    history_list = []
    for row in history:
        # Format the timestamp to a readable format
        timestamp = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
        formatted_time = timestamp.strftime('%b %d, %Y %H:%M')
        history_list.append({
            'wpm': row[0],
            'accuracy': row[1],
            'difficulty': row[2],
            'timestamp': formatted_time
        })
    return jsonify(history_list)

if __name__ == '__main__':
    # Initialize database if it doesn't exist
    if not os.path.exists(DATABASE):
        init_db()
    app.run(debug=True)