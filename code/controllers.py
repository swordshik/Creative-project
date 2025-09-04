# controllers.py
from models import TaskModel, SolversModel, LeaderboardModel
from datetime import datetime

class AppController:
    def __init__(self, db):
        self.tasks = TaskModel(db)
        self.solvers = SolversModel(db)
        self.leaderboard = LeaderboardModel(db)

    def get_today_task(self):
        return self.tasks.get_today_task()

    def get_solvers_today(self):
        return self.solvers.get_solvers_for_today()

    def get_leaderboard(self):
        return self.leaderboard.get_top_solvers()
