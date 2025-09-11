prompt_topping = "How many Toppings would you like the pizza to have?\n "

topping_amount = int(input(prompt_topping))
while True:
    if topping_amount <= 0:
        print("You don't have any more ingredients to add to the pizza, bye!")
        break
    elif topping_amount > 0:
        topping_name = input("Enter your favorite topping: ")
        print(f"{topping_name} was added to the pizza doughs!")
        topping_amount -= 1
