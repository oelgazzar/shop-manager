import tkinter as tk
from tkinter import messagebox

from .header_frame import HeaderFrame
from .toolbar_frame import ToolbarFrame
from .product_list_frame import ProductListFrame
from .product_details_frame import ProductDetailsFrame
from .product_form_view import ProductFormView
from models.product import Product

class ProductView(tk.Frame):
    def __init__(self, master, db):
        super().__init__(master)

        self.db = db
        self.search_query = tk.StringVar()
        self.search_query.trace_add('write', lambda *_: self._update_product_list())

        self._create_widgets()
        self._layout_widgets()

        self._update_product_list()

    def _create_widgets(self):
        self.header_frame = HeaderFrame(self,)
        self.toolbar_frame = ToolbarFrame(self, search_query_variable=self.search_query,
                                          on_add_product_clicked=self.show_product_form_window)
        self.product_list_frame = ProductListFrame(self, on_item_selected=self.update_product_details)
        self.product_details_frame = ProductDetailsFrame(self,
                                                        on_delete_button_clicked=self._delete_product,
                                                        on_edit_button_clicked=self.show_product_form_window,
                                                        on_hide_button_clicked=lambda: self.toggle_product_details_frame(False),
                                                        width=300)
        self.product_details_frame.pack_propagate(False)

    def _layout_widgets(self):
        self.header_frame.pack(fill='x', pady='0 30')
        self.toolbar_frame.pack(fill='x')
        self.product_list_frame.pack(fill='both', expand=1, pady='30 0', side='left')

    def _update_product_list(self):
        self.product_list_frame.update(self.db.get_all_products(self.search_query.get()))

    def update_product_details(self, product_id):
        if product_id is None:
            self.product_details_frame.update(None)
            self.toggle_product_details_frame(False)
            return
        
        product = self.db.get_product(product_id)
        if product is None:
            return
        self.product_details_frame.update(product)
        self.toggle_product_details_frame(True)

    def toggle_product_details_frame(self, show):
        if show:
            self.product_details_frame.pack(fill='both', expand=1, side='left', pady='30 0', padx='10 0')
        else:
            self.product_details_frame.pack_forget()

    def show_product_form_window(self, product=None):
        ProductFormView(self, db=self.db, save_handler=self._add_edit_products, product=product)

    def _add_edit_products(self, product, values):
        if product is None:
            product = Product(None, *values)
            self.db.create_product(product)
        else:
            (product.name, product.price, product.stock) = values
            self.db.update_product(product)
        self._refresh()

    def _refresh(self):
        self._update_product_list()

    def _delete_product(self, product):
        response = messagebox.askyesno(title="Confirm Delete Product", message=f"""Are you sure to delete this product
        [ {product.name} ]""")
        if not response: return

        self.db.delete_product(product)
        self.update_product_details(None)
        self._refresh()
