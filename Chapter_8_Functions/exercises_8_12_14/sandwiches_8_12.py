def sandwich_ingredients(*ingredients):
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")

print("First List: ")
sandwich_ingredients('cheese', 'chicken', 'lettuce','tomatoes', 'avocado', 'olives', 'onions', 'salad dress')

print("Second List: ")
sandwich_ingredients('meat balls', 'cheddar cheese', 'tomatoes', 'bacon')

print("Third List: ")
sandwich_ingredients('chicharron', 'gouda cheese', 'bacon')