import tkinter as tk
from constants import MODES, ABOUT_TEXT, CREATOR_TEXT
from tkinter import messagebox
class AppMenu:

    def __init__(self, root, change_mode_callback):
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Справка", menu=help_menu)

        help_menu.add_command(
            label="О программе",
            command=self.show_about
        )
        help_menu.add_command(
            label="Создатель",
            command=self.show_creator
        )

        mode_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Режим", menu=mode_menu)

        for key, value in MODES.items():
            mode_menu.add_command(
                label=value,
                command=lambda k=key: change_mode_callback(k)
            )

        self.menu.add_command(label="Выход", command=root.quit)

    def show_about(self):
        messagebox.showinfo(
            "О программе",
            ABOUT_TEXT
        )

    def show_creator(selfself):
        messagebox.showinfo("Кем создано", CREATOR_TEXT)