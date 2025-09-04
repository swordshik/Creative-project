# ui.py
import tkinter as tk
from tkinter import ttk

class AppUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Daily Challenge Hub")
        self.root.geometry("800x600")
        
        self.task_frame = tk.Frame(root, bg="white", relief="solid", borderwidth=1)
        self.task_frame.place(relx=0.05, rely=0.05, relwidth=0.45, relheight=0.4)
        
        self.solver_frame = tk.Frame(root, bg="white", relief="solid", borderwidth=1)
        self.solver_frame.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.4)
        
        self.leaderboard_frame = tk.Frame(root, bg="white", relief="solid", borderwidth=1)
        self.leaderboard_frame.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.4)
        
        self.update_ui()

    def update_ui(self):
        for frame in [self.task_frame, self.solver_frame, self.leaderboard_frame]:
            for widget in frame.winfo_children():
                widget.destroy()

        task = self.controller.get_today_task()
        if task:
            tk.Label(self.task_frame, text=f"Задача: {task[0]}", font=("Arial", 14, "bold")).pack()
            tk.Label(self.task_frame, text=task[1], wraplength=300, font=("Arial", 12)).pack()

        tk.Label(self.solver_frame, text="Список решивших", font=("Arial", 14, "bold")).pack()
        solvers = self.controller.get_solvers_today()
        for name, solved_at in solvers:
            tk.Label(self.solver_frame, text=f"{name} — {solved_at}").pack(anchor="w")

        tk.Label(self.leaderboard_frame, text="Топы за всё время", font=("Arial", 14, "bold")).pack()
        leaderboard = self.controller.get_leaderboard()
        for name, total in leaderboard:
            tk.Label(self.leaderboard_frame, text=f"{name}: {total}").pack(anchor="w")

        self.root.after(5000, self.update_ui)  # обновление каждые 5 секунд

if __name__ == "__main__":
    root = tk.Tk()
    # Здесь должен быть инициализирован контроллер, например:
    # controller = AppController(Database())
    # app = AppUI(root, controller)
    root.mainloop()