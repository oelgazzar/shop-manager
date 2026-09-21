import tkinter as tk
from tkinter import ttk

from .header_frame import HeaderFrame
from .toolbrar_frame import ToolbarFrame
from .product_list_frame import ProductListFrame
from .product_details_frame import ProductDetailsFrame

class ProductView(tk.Frame):
    def __init__(self, master, db):
        super().__init__(master)

        self.db = db

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):
        self.header_frame = HeaderFrame(self)
        self.toolbar_frame = ToolbarFrame(self)
        self.product_list_frame = ProductListFrame(self, self.db)
        self.product_details_frame = ProductDetailsFrame(self, self.db, width=300)
        self.product_details_frame.pack_propagate(False)

    def _layout_widgets(self):
        self.header_frame.pack(fill='x', pady='0 30')
        self.toolbar_frame.pack(fill='x')
        self.product_list_frame.pack(fill='both', expand=1, pady='30 0', side='left')

    def toggle_product_details(self, show):
        if show:
            self.product_details_frame.pack(fill='both', expand=1, side='left', pady='30 0', padx='10 0')
        else:
            self.product_details_frame.pack_forget()
