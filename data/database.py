import sqlite3

from models.product import Product

schema = '''
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    stock INTEGER NOT NULL
);
'''

class Database:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self._init_schema()

    def _init_schema(self):
        with self.connection as con:
            con.executescript(schema)

    def get_all_products(self, name_filter=''):
        with self.connection as con:
            res = con.execute('SELECT * FROM products WHERE NAME LIKE ?', (f'%{name_filter}%',))
            return [Product(*values) for values in res.fetchall()]

    def get_product(self, product_id):
            with self.connection as con:
                res = con.execute('SELECT * FROM products WHERE id = ?', (product_id,))
                return Product(*res.fetchone())

    def create_product(self, product):
        with self.connection as con:
            return con.execute('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)',
                        (product.name, product.price, product.stock))

    def update_product(self, product):
        with self.connection as con:
            return con.execute('UPDATE products SET name = ?, price = ?, stock = ? WHERE id = ?',
                               (product.name, product.price, product.stock, product.id))

    def delete_product(self, product):
        with self.connection as con:
            return con.execute('DELETE FROM products WHERE id = ?', (product.id,))

    def close(self):
        self.connection.close()