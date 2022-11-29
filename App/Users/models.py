from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, username, role, password, is_admin=False):
        self.id = id
        self.username = username
        self.role = role
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def get_id(self):
        print(f"ID DEL SUPER USUARIO {super().get_id()}")
        return super().get_id()

