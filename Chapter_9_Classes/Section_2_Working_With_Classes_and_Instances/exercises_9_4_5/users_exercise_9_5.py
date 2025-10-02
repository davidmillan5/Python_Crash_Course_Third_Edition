class User:
    """Create a user instance with several data on it"""

    def __init__(self, name, last, username, email):
        """Create an instance of the class user with important attributes"""
        self.name = name
        self.last_name = last
        self.username = username
        self.mail = email
        self.login_attempts = 0


    def describe_user(self):
        """method to print basic info about the user"""
        print(f"\nname: {self.name} \nlast name: {self.last_name} \nusername: {self.username} \nmail: {self.mail}")

    def greet_user(self):
        """method to greet the connected users"""
        print(f"Welcome back {self.username.title()}!")


    def increment_login_attempts(self):
        """Increment the value of logging attempts by 1"""
        self.login_attempts += 1
        print(f"You have attempts to login {self.login_attempts} !")

    def reset_login_attempts(self):
        """Resets the value of logging_attempts"""
        self.login_attempts = 0
        print(f"You have {self.login_attempts} attempts to login.")


user_200 = User('eren','yaeger','shingekynokyojin','rumbling@paradis.com')

user_200.increment_login_attempts()
user_200.increment_login_attempts()
user_200.increment_login_attempts()
user_200.increment_login_attempts()
user_200.increment_login_attempts()
user_200.increment_login_attempts()

user_200.reset_login_attempts()