sandwich_orders = [
    "BLT",
    "Grilled Cheese",
    "Turkey Club",
    "pastrami",
    "Ham and Swiss",
    "Reuben",
    "Italian Sub",
    "pastrami",
    "Chicken Caesar Wrap",
    "Tuna Melt",
    "Philly Cheesesteak",
    "Veggie Deluxe",
    "Cuban Sandwich",
    "Club Sandwich",
    "pastrami",
]
finished_sandwiches = []


# Removing all instances of specific value

print(f"The deli has run out of pastrami!, we will not make more sandwiches of it....")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:

    current_sandwich = sandwich_orders.pop()

    print(f"The {current_sandwich.title()} is being prepared...")
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches

print(f"\nThe following sandwiches has been prepared: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
