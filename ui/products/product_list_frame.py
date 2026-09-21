import tkinter as tk
from tkinter import ttk

class ProductListFrame(tk.Frame):
    def __init__(self, master, on_item_selected, **cnf):
        super().__init__(master, **cnf)

        self.on_item_selected = on_item_selected

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        self.product_list = ttk.Treeview(self, columns=('name', 'price', 'stock'), show='headings')
        self.product_list.heading('name', text='Name')
        self.product_list.heading('price', text='Price')
        self.product_list.heading('stock', text='Stock')
        self.product_list.bind('<<TreeviewSelect>>', self._on_list_selection_changed)

    def _layout_widgets(self):
        self.product_list.pack(fill='both', expand=1)

    def update(self, products):
        for item in self.product_list.get_children():
            self.product_list.delete(item)

        for product in products:
            self.product_list.insert('', 'end', iid=product.id, values=(product.name, product.price, product.stock))

    def _on_list_selection_changed(self, _):
        selected_items = self.product_list.selection()
        if selected_items:
            selected_product_id = selected_items[0]
            self.on_item_selected(selected_product_id)
        else:
            self.on_item_selected(None)

    def scroll_to_end(self):
        self.product_list.yview_moveto(1)
                                      