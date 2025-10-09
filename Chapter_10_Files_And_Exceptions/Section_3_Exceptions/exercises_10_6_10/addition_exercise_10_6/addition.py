"""Addition Function to sum two numbers"""


def addition(number_1, number_2):
    """Function to add 2 numbers"""
    sum_numbers = number_1 + number_2
    return sum_numbers



def input_numbers():
    """Function to input numbers to execute other functions"""

    try:
        number_1 = int(input("\nEnter your first number: "))
        number_2 = int(input("Enter your second number: "))
    except ValueError:
        print("You should enter a valid number! ")
    else:
        print("The sum is:", addition(number_1, number_2))


input_numbers()