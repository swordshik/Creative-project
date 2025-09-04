# setup_db.py
import sqlite3
from datetime import datetime, timedelta

def setup():
    conn = sqlite3.connect("daily_challenge.db")
    c = conn.cursor()

    # Создаём таблицы
    c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT UNIQUE,
                    title TEXT,
                    description TEXT
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS solvers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_date TEXT,
                    name TEXT,
                    solved_at TEXT
                )""")

    c.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    total_solved INTEGER
                )""")

    # Добавляем тестовые данные
    today = datetime.now().date()
    c.execute("INSERT OR IGNORE INTO tasks (date, title, description) VALUES (?, ?, ?)",
              (str(today), "Задача дня", "Найти сумму чисел от 1 до N"))

    c.execute("INSERT OR IGNORE INTO leaderboard (name, total_solved) VALUES (?, ?)", ("Али", 5))
    c.execute("INSERT OR IGNORE INTO leaderboard (name, total_solved) VALUES (?, ?)", ("Айгерим", 3))
    c.execute("INSERT OR IGNORE INTO leaderboard (name, total_solved) VALUES (?, ?)", ("Бек", 2))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup()
    print("Database initialized.")