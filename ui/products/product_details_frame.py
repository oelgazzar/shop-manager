import tkinter as tk
from tkinter import ttk

class ProductDetailsFrame(tk.LabelFrame):
    def __init__(self, master, db, **cnf):
        super().__init__(master, **cnf)

        self.db = db
        self.config(text="Patient Details")

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        self.name_label = ttk.Label(self, text="Name: Mouse")
        self.price_label = ttk.Label(self, text='Price: 13$')
        self.stock_label = ttk.Label(self,text='Stock: 14')
        self.edit_button = ttk.Button(self, text='Edit')
        self.delete_button = ttk.Button(self, text='Delete')

    def _layout_widgets(self):
        self.name_label.pack(fill='x', padx=10, pady=10)
        self.price_label.pack(fill='x', padx=10, pady=10)
        self.stock_label.pack(fill='x', padx=10, pady=10)
        self.edit_button.pack(side='left', fill='x', padx=10, pady=10)
        self.delete_button.pack(side='left', fill='x', padx=10, pady=10)