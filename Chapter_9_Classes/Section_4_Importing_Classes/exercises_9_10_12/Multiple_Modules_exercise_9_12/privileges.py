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

