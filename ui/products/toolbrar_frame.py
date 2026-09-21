import tkinter as tk
from tkinter import ttk

class ToolbarFrame(tk.Frame):
    def __init__(self, master, **cnf):
        super().__init__(master, **cnf)

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        self.search_label = ttk.Label(self, text="Search:")
        self.search_entry = ttk.Entry(self, width=50)
        self.add_button = ttk.Button(self, text="Add Product")

    def _layout_widgets(self):
        self.search_label.pack(side='left', padx='0 10')
        self.search_entry.pack(side='left')
        self.add_button.pack(side='right', padx='20 0')
                                      