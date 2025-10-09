"""Addition Calculator"""

def addition_calculator(number_1, number_2):
    """Function to add two different numbers"""
    addition = number_1 + number_2
    return f"Your total is {addition}"

def calculator_values():
    """Function to capture the values to the addition"""
    try:
        number_1 = int(input("Enter the first numerical value: "))
        number_2 = int(input("Enter the second numerical value: "))
    except ValueError:
        print("The character that you enter for the calculator is not a number.")
    else:
        print(f"The result of your addition is = {addition_calculator(number_1, number_2)}")


def calculator_exec():
    """Function to execute the calculator"""
    while True:
        print("Prepare to launch the calculator console")
        calculator_values()
        quitter = input("If you want to exit enter 'q' if not enter any other value to the console: \n")
        if quitter == 'q':
            break

calculator_exec()