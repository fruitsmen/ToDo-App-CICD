from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Подключение к PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="todolist",
        user="todouser",
        password="password",
        host="localhost"
    )
    return conn

# Создание таблицы задач
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            task TEXT NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO tasks (task) VALUES (%s)', (task,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
