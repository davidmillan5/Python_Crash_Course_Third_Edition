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


class IceCreamStand(Restaurant):
    """A Class That Inherit attributes and methods from a parent Restaurant class"""

    def __init__(self,restaurant_name,cuisine_type, flavors):
        """Initialize attributes of the parent class."""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors


    def list_of_flavors(self):
        """Print a list of  ice cream flavors"""
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print(f" - {flavor.title()}.")


gelateria = IceCreamStand('gelateria', 'italian', ['cherry', 'choco rochelle', 'lemon pie','blueberries'])



gelateria.describe_restaurant()
gelateria.open_restaurant()
gelateria.list_of_flavors()