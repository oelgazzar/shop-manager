import tkinter as tk

from data.database import Database
from ui.products.product_view import ProductView

db = Database("shop.db")

root = tk.Tk()
root.title("Shop Manager")
product_view = ProductView(root, db)
product_view.pack(fill='both', expand=True, padx=10, pady=10)
root.mainloop()