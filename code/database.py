# database.py
import sqlite3

class Database:
    def __init__(self, db_name="daily_challenge.db"):
        self.db_name = db_name

    def query(self, sql, params=(), fetchone=False, fetchall=False):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        result = None
        if fetchone:
            result = cursor.fetchone()
        elif fetchall:
            result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result
