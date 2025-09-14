# Function to make a shirt

def make_shirt(shirt_size, shirt_message):
    """A Function to create a shirt and a message on it"""
    print(f"\nYou have ordered a shirt size: {shirt_size}.")
    print(f"And the message on the shirt is going to be: {shirt_message.title()} ")


def shirt_information():
    input_size = input("\nHello! What size of shirt do you want us to make: ")
    input_message = input("\nWhat message do you want on the shirt to be print it out: ")

    make_shirt(input_size, input_message)

def shirt_amount():
    amount = True
    quantity = int(input("How many shirts do you want to make? "))
    order_number = 0
    while amount:
        if quantity > 0:
            order_number +=1
            print(f"Order # {order_number}")
            shirt_information()
            quantity -= 1
            print("\n----- We are working on your new order ------")
        if quantity == 0:
            amount = False
            print("\n ----- You don't have anymore order left --------")
            print(" ----- Thanks for coming by --------")

shirt_amount()