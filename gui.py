import tkinter as tk
from tkinter import messagebox
from Calculations import FinancialCalculator
from constants import *
from menu import AppMenu

class FinancialApp:

    def __init__(self, root):
        self.root = root
        self.root.title(TITLE)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.resizable(True, True)

        self.mode = "annuity_payment"

        AppMenu(root, self.change_mode)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Сумма:").grid(row=0, column=0)
        self.entry_sum = tk.Entry(self.root)
        self.entry_sum.grid(row=0, column=1)

        tk.Label(self.root, text="Ставка (%):").grid(row=1, column=0)
        self.entry_rate = tk.Entry(self.root)
        self.entry_rate.grid(row=1, column=1)

        tk.Label(self.root, text="Срок (лет):").grid(row=2, column=0)
        self.entry_years = tk.Entry(self.root)
        self.entry_years.grid(row=2, column=1)

        self.result = tk.Label(self.root, text="Результат:")
        self.result.grid(row=4, column=0, columnspan=2)

        tk.Button(self.root, text="Рассчитать", command=self.calculate)\
            .grid(row=3, column=0, columnspan=2)

    def change_mode(self, mode):
        self.mode = mode
        messagebox.showinfo("Режим", f"Выбран режим: {mode}")

    def calculate(self):
        try:
            s = float(self.entry_sum.get())
            r = float(self.entry_rate.get())
            y = float(self.entry_years.get())

            calc = FinancialCalculator()

            if self.mode == "annuity_payment":
                res = calc.annuity_payment(s, r, y)
                text = f"Ежемесячный платеж: {res:.2f}"
            elif self.mode == "compound_interest":
                res = calc.compound_interest(s, r, y)
                text = f"Итоговая сумма: {res:.2f}"
            else:
                res = calc.simple_interest(s, r, y)
                text = f"Доход: {res:.2f}"

            self.result.config(text=text)

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
