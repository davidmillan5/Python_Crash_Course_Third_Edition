class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """
        Set the odometer reading to given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """Ad the given amount to the odometer reading."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a24', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

### Modifying an Attribute's Value Directly

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

### Modifying an Attribute's Value Through a Method

my_new_car.update_odometer(55)
my_new_car.read_odometer()

my_new_car.update_odometer(5)
my_new_car.read_odometer()

### Incrementing an Attribute's Value Through a Method

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()