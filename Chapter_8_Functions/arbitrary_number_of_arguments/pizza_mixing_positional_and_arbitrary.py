def make_pizza(size,*toppings):
    """Summarize the pizza_importing_entire_module we are about to make."""
    print(f"\nMaking a {size}-inch pizza_importing_entire_module with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza(16,'mushrooms', 'peppers', 'gouda cheese', 'pepperoni')
