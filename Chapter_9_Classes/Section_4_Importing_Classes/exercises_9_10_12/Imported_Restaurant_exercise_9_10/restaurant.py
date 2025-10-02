class Restaurant:
    """A simple class to create a restaurant object"""

    def __init__(self,restaurant_name,cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """Print the information related to the object restaurant"""
        print(f"Our restaurant name is {self.restaurant_name.title()} and we prepare {self.cuisine_type.title()}!")

    def open_restaurant(self):
        """Print open message"""
        print(f"The {self.restaurant_name.title()} restaurant is open!")