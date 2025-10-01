class Restaurant:
    """A simple class to create a restaurant object"""

    def __init__(self,restaurant_name,cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served = 0


    def describe_restaurant(self):
        """Print the information related to the object restaurant"""
        print(f"Our restaurant name is {self.restaurant_name.title()} and we prepare {self.cuisine_type.title()} cuisine!")

    def open_restaurant(self):
        """Print open message"""
        print(f"The {self.restaurant_name.title()} restaurant is open!")

    def numbered_served(self):
        """Print the number of customers the restaurant has served"""
        print(f"The restaurant has served {self.served} customers today.")

    def set_number_served(self,number_served):
        """Let us set the number of customers that have been served."""
        self.served = number_served
        print(f"The restaurant has served {self.served} customers today.")

    def increment_number_served(self,number_served):
        """Let us increment the number of customers who've been served"""
        self.served += number_served
        print(f"The restaurant has served {self.served} customers today.")


le_figaro = Restaurant('le figaro','french')
le_figaro.describe_restaurant()

le_figaro.open_restaurant()

le_figaro.numbered_served()

le_figaro.set_number_served(9)

le_figaro.increment_number_served(11)