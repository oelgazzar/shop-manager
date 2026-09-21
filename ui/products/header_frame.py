import tkinter as tk
from tkinter import ttk

class HeaderFrame(tk.Frame):
    def __init__(self, master, **cnf):
        super().__init__(master, **cnf)

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        self.header_label = ttk.Label(self, text="Products",
                                      font="Ubuntu 24 bold")

    def _layout_widgets(self):
        self.header_label.pack(fill='x')
                                      