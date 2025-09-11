prompt_topping = "Which Topping would you like the pizza to have?\n "

topping = ""
while topping != 'quit':
    topping = input(prompt_topping)

    if topping != 'quit':
        print(f"{topping.title()} was added to the pizza!")

