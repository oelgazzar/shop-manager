import tkinter as tk
from tkinter import ttk

from models.product import Product

class ProductFormView(tk.Toplevel):
    def __init__(self, master, db, on_save, product=None, **cnf):
        super().__init__(master, **cnf)

        self.db = db
        self.on_save = on_save
        self.product = product

        self.product_name_var = tk.StringVar(value=self.product.name if self.product else '')
        self.product_price_var = tk.StringVar(value=self.product.price if self.product else '')
        self.product_stock_var = tk.StringVar(value=self.product.stock if self.product else '')

        self.transient(master)
        self.grab_set()
        self.config(padx=10, pady=10)

        x = master.winfo_x() + (master.winfo_width() - self.winfo_width()) // 2
        y = master.winfo_y() + (master.winfo_height() - self.winfo_height()) // 2


        self._create_widgets()
        self._layout_widgets()

        self.geometry(f"+{x}+{y}")

    def _create_widgets(self):
        self.title_label = ttk.Label(self, text='New Product' if self.product is None else 'Update Product',
                                     font='Ubuntu 24 bold')
        self.name_label = ttk.Label(self, text='Name:')
        self.name_entry = ttk.Entry(self, textvariable=self.product_name_var)
        self.price_label = ttk.Label(self, text='Price:')
        self.price_entry = ttk.Entry(self, textvariable=self.product_price_var)
        self.stock_label = ttk.Label(self, text='Stock:')
        self.stock_entry = ttk.Entry(self, textvariable=self.product_stock_var)
        self.save_button = ttk.Button(self, text='Save', command=self._on_save_clicked)

    def _layout_widgets(self):
        self.title_label.grid(row=0, columnspan=2, pady='0 10', sticky='we')
        self.name_label.grid(row=1, column=0, pady=10)
        self.name_entry.grid(row=1, column=1)
        self.price_label.grid(row=2, column=0, pady=10)
        self.price_entry.grid(row=2, column=1)
        self.stock_label.grid(row=3, column=0, pady=10)
        self.stock_entry.grid(row=3, column=1)
        self.save_button.grid(row=4, columnspan=2, pady=10)

    def _on_save_clicked(self):
        self._save()
        self.destroy()
        self.on_save()

    def _save(self):
        name = self.product_name_var.get()
        price = self.product_price_var.get()
        stock = self.product_stock_var.get()

        if self.product is None:
            product = Product(id=None, name=name, price=price, stock=stock)
            self.db.create_product(product)
        else:
            self.product.name = name
            self.product.price = price
            self.product.stock = stock
            self.db.update_product(self.product)