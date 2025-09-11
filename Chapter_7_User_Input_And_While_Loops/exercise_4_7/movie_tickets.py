prompt_age = "Based on your age the ticket prices vary, How old are you? \n"

age = ""

while age != 'quit':
    age = int(input(prompt_age))

    if age < 3:
        print("The Ticket is free!")
    elif age < 12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")