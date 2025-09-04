# models.py
from database import Database
from datetime import datetime

class TaskModel:
    def __init__(self, db: Database):
        self.db = db

    def get_today_task(self):
        today = str(datetime.now().date())
        return self.db.query("SELECT title, description FROM tasks WHERE date = ?", (today,), fetchone=True)

class SolversModel:
    def __init__(self, db: Database):
        self.db = db

    def get_solvers_for_today(self):
        today = str(datetime.now().date())
        return self.db.query("SELECT name, solved_at FROM solvers WHERE task_date = ? ORDER BY solved_at DESC",
                             (today,), fetchall=True)

class LeaderboardModel:
    def __init__(self, db: Database):
        self.db = db

    def get_top_solvers(self, limit=5):
        return self.db.query("SELECT name, total_solved FROM leaderboard ORDER BY total_solved DESC LIMIT ?",
                             (limit,), fetchall=True)
