from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from App.Users.controller import *

class User(UserMixin):
    def __init__(self, id, username, role, password, is_admin=False):
        self.id = id
        self.username = username
        self.role = role
        self.password = generate_password_hash(password)
        self.is_active=True
        self.is_admin = is_admin
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return '<User {}>'.format(self.email)

    
    
def get_user(username):
    try:
        user = get_users(userDict = {"username":username})
        return user
    except Exception as e:
        return f"Fatal Error. {e}"