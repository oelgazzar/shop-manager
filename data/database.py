import sqlite3

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

    def get_all_products(self):
        with self.connection as con:
            res = con.execute('SELECT * FROM products')
            return res.fetchall()

    def close(self):
        self.connection.close()