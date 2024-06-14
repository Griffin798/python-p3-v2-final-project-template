import sqlite3

# from models.database import get_connection

DATABASE = 'finance_manager.db'

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    
    def save(self):
        self.create(self.username, self.password, self.email)
    # def save(self):
    #     conn = get_connection()
    #     cursor = conn.cursor()
    #     cursor.execute('''
    #         INSERT INTO users (username, password, email) VALUES (?, ?, ?)
    #     ''', (self.username, self.password, self.email))
    #     conn.commit()
    #     conn.close()

    @classmethod
    def create(cls, username, password, email):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
            conn.commit()

    @classmethod
    def delete(cls, user_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()

    @classmethod
    def get_all(cls):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM users')
            return c.fetchall()

    @classmethod
    def find_by_id(cls, user_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            return c.fetchone()