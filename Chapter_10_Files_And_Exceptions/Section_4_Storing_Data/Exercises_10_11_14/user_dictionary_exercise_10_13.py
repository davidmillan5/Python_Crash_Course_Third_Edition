from pathlib import Path
import json

def get_stored_user_data(path):
    """Get stored username if available"""
    if path.exists():
        contents = path.read_text()
        userdata = json.loads(contents)
        return userdata
    else:
        return None

def get_new_user_data(path):
    """Prompt for a new username."""
    user_data = []
    username = input("What is your name? ")
    user_data.append(username)
    user_age = input("How old are you? ")
    user_data.append(user_age)
    user_mail = input("Enter your email? ")
    user_data.append(user_mail)
    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data

def greet_user():
    """Greet the user by name."""
    path = Path('userdata.json')
    user_data = get_stored_user_data(path)
    if user_data:
        print(f"Welcome back, {user_data[0]}")
    else:
        get_new_user_data(path)
        print(f"We'll remember you when you come back")

greet_user()