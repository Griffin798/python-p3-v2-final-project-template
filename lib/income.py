import sqlite3

DATABASE = 'finance_manager.db'

class Income:
    def __init__(self, source, amount, date, user_id):
        self.source = source
        self.amount = amount
        self.date = date
        self.user_id = user_id

    @classmethod
    def create(cls, source, amount, date, user_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO income (source, amount, date, user_id) VALUES (?, ?, ?, ?)', 
                      (source, amount, date, user_id))
            conn.commit()

    @classmethod
    def delete(cls, income_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('DELETE FROM income WHERE id = ?', (income_id,))
            conn.commit()

    @classmethod
    def get_all(cls, user_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM income WHERE user_id = ?', (user_id,))
            return c.fetchall()

    @classmethod
    def find_by_id(cls, income_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM income WHERE id = ?', (income_id,))
            return c.fetchone()
