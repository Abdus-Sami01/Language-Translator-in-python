import sqlite3

class Database:
    def __init__(self, db_name="app.db"):
        self.db_name = db_name

    def connect(self):
        """Establishes a database connection and initializes tables."""
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates necessary tables for users and tasks."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        self.conn.commit()

    def add_user(self, username, password):
        """Adds a new user to the database."""
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Username already exists

    def get_user(self, username):
        """Retrieves a user by username."""
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()

    def add_task(self, user_id, title, description):
        """Adds a new task for a user."""
        self.cursor.execute("INSERT INTO tasks (user_id, title, description) VALUES (?, ?, ?)", (user_id, title, description))
        self.conn.commit()

    def get_tasks(self, user_id):
        """Retrieves all tasks for a user."""
        self.cursor.execute("SELECT * FROM tasks WHERE user_id = ?", (user_id,))
        return self.cursor.fetchall()

    def update_task_status(self, task_id, status):
        """Updates the status of a task."""
        self.cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        """Deletes a task by ID."""
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()

    def close(self):
        """Closes the database connection."""
        self.conn.close()
