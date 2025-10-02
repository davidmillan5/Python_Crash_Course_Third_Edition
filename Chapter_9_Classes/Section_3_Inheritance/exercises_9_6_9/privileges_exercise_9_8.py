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



class Privileges:
    """Create an instance of privileges to be applied to admin users"""

    def __init__(self,privileges = ['add user', 'can add post', 'can ban user', 'can delete post']):
        """Create an instance of privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Methods to print the admin privileges"""
        print("The admin list of privileges are: \n")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    """Create a special kind of user"""

    def __init__(self,name,last,username,email):
        """Create an instance that inherit from the parent class user"""
        super().__init__(name,last,username,email)
        self.privileges = Privileges()


admin_2 = Admin('eren', 'yaeger', 'eyaeger','rumbling@paradis.eu')

admin_2.privileges.show_privileges()

