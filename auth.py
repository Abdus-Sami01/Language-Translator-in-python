import hashlib
import Database

class Auth:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def hash_password(self, password):
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        """Registers a new user."""
        hashed_password = self.hash_password(password)
        return self.db.add_user(username, hashed_password)

    def authenticate_user(self, username, password):
        """Authenticates a user."""
        user = self.db.get_user(username)
        if user and user[2] == self.hash_password(password):  # user[2] is the stored password
            return True
        return False

    def close_connection(self):
        """Closes the database connection."""
        self.db.close()
