import tkinter as tk
from tkinter import ttk

class ProductListFrame(tk.Frame):
    def __init__(self, master, db, **cnf):
        super().__init__(master, **cnf)

        self.db = db

        self._create_widgets()
        self._layout_widgets()
        self._populate_list()

    def _create_widgets(self):
        self.product_list = ttk.Treeview(self, columns=('name', 'price', 'stock'), show='headings')
        self.product_list.heading('name', text='Name')
        self.product_list.heading('price', text='Price')
        self.product_list.heading('stock', text='Stock')

    def _layout_widgets(self):
        self.product_list.pack(fill='both', expand=1)

    def _populate_list(self):
        products = self.db.get_all_products()
        for item in products:
            self.product_list.insert('', 'end', iid=item[0], values=item[1:])
                                      