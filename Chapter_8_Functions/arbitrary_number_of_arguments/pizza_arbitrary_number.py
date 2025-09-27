def make_pizza(*toppings):
    """Summarize the pizza_importing_entire_module we are about to make."""
    print("\nMaking a pizza_importing_entire_module with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza('mushrooms', 'peppers', 'gouda cheese', 'pepperoni')
