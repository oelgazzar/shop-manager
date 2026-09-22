import tkinter as tk
from tkinter import ttk

class ProductDetailsFrame(tk.LabelFrame):
    def __init__(self, master, on_edit_button_clicked, on_delete_button_clicked,
                 on_hide_button_clicked, **cnf):
        super().__init__(master, **cnf)

        self.product = None

        self.on_edit_button_clicked = on_edit_button_clicked
        self.on_delete_button_clicked = on_delete_button_clicked
        self.on_hide_button_clicked = on_hide_button_clicked

        self.config(text="Product Details")

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        self.name_label = ttk.Label(self, text="Name:")
        self.name_value = ttk.Label(self)
        self.price_label = ttk.Label(self, text='Price:')
        self.price_value = ttk.Label(self)
        self.stock_label = ttk.Label(self,text='Stock:')
        self.stock_value = ttk.Label(self)
        self.edit_button = ttk.Button(self, text='Edit', command=lambda: self.on_edit_button_clicked(self.product))
        self.delete_button = ttk.Button(self, text='Delete', command=lambda: self.on_delete_button_clicked(self.product))
        self.hide_button = ttk.Button(self, text='Hide>>', command=self.on_hide_button_clicked)

    def _layout_widgets(self):
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
        self.name_value.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        self.price_label.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.price_value.grid(row=1, column=1, padx=10, pady=10, sticky='ew')
        self.stock_label.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        self.stock_value.grid(row=2, column=1, padx=10, pady=10, sticky='ew')
        self.edit_button.grid(row=3, column=0, padx=10, pady=10, sticky='ew')
        self.delete_button.grid(row=3, column=1, padx=10, pady=10, sticky='ew')
        self.hide_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    def update(self, product):
        self.product = product
        if product is None:
            self.name_value['text'] = ''
            self.price_value['text'] = ''
            self.stock_value['text'] = ''
            return

        self.name_value['text'] = product.name
        self.price_value['text'] = product.price
        self.stock_value['text'] = product.stock