users_db = {}

def add_user(user):
    users_db[user.email] = user

def get_user_by_email(email):
    return users_db.get(email)    