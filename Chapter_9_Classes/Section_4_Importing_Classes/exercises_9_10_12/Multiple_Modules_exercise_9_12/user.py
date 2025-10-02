class User:
    """Create a user instance with several data on it"""

    def __init__(self, name, last, username, email):
        """Create an instance of the class user with important attributes"""
        self.name = name
        self.last_name = last
        self.username = username
        self.mail = email


    def describe_user(self):
        """method to print basic info about the user"""
        print(f"\nname: {self.name} \nlast name: {self.last_name} \nusername: {self.username} \nmail: {self.mail}")

    def greet_user(self):
        """method to greet the connected users"""
        print(f"Welcome back {self.username.title()}!")
