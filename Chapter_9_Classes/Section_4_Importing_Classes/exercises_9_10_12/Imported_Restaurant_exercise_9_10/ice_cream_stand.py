from restaurant import Restaurant

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