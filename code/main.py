from tkinter import Tk
from database import Database
from controllers import AppController
from ui import AppUI

if __name__ == "__main__":
    db = Database()
    controller = AppController(db)
    root = Tk()
    app = AppUI(root, controller)
    root.mainloop()
