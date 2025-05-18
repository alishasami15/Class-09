from models import User
from db import add_user, get_user_by_email

def register_user(name, email, password):
    if get_user_by_email(email):
          return False, "User already exists!"
    user = User(name, email, password)
    add_user(user)
    return True, user

def login_user(email, password):
     user = get_user_by_email(email)
     if user and user.password == password:
          return True, user
     else:
          return False, "Invalid credentials"