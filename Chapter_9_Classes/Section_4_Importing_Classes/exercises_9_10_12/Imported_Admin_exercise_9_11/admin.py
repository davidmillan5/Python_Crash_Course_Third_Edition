from user import User
from privileges import Privileges


class Admin(User):
    """Create a special kind of user"""

    def __init__(self,name,last,username,email):
        """Create an instance that inherit from the parent class user"""
        super().__init__(name,last,username,email)
        self.privileges = Privileges()