import sqlite3

DATABASE = 'finance_manager.db'

class SavingsGoal:
    def __init__(self, goal_name, target_amount, user_id):
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.user_id = user_id

    @classmethod
    def create(cls, goal_name, target_amount, user_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO savings_goals (goal_name, target_amount, user_id) VALUES (?, ?, ?)', 
                      (goal_name, target_amount, user_id))
            conn.commit()

    @classmethod
    def delete(cls, goal_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('DELETE FROM savings_goals WHERE id = ?', (goal_id,))
            conn.commit()

    @classmethod
    def get_all(cls, user_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM savings_goals WHERE user_id = ?', (user_id,))
            return c.fetchall()

    @classmethod
    def find_by_id(cls, goal_id):
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM savings_goals WHERE id = ?', (goal_id,))
            return c.fetchone()
