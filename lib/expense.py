import sqlite3

DATABASE = 'finance_manager.db'

class Expense:
    def __init__(self, description, amount, date, user_id):
        self.description = description
        self.amount = amount
        self.date = date
        self.user_id = user_id

    @classmethod
    def create(cls, description, amount, date, user_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO expenses (description, amount, date, user_id) VALUES (?, ?, ?, ?)', 
                      (description, amount, date, user_id))
            conn.commit()

    @classmethod
    def delete(cls, expense_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
            conn.commit()

    @classmethod
    def get_all(cls, user_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM expenses WHERE user_id = ?', (user_id,))
            return c.fetchall()

    @classmethod
    def find_by_id(cls, expense_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM expenses WHERE id = ?', (expense_id,))
            return c.fetchone()
