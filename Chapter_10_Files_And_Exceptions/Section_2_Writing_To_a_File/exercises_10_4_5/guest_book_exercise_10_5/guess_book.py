from pathlib import Path

print("----- Welcome to the new guest book -------")
print("-------Enter the name of a new user or 'q' to quit the system --------")

path = Path('guest_book.txt')

while True:
    guest_name = input("--- Enter your name: --------- \n")

    if guest_name.lower() == 'q':
        break

    # Use 'a' mode to append instead of overwriting
    with path.open('a') as file:
        file.write(f"{guest_name}\n")

    print(f"Welcome, {guest_name}! Your name has been added.\n")

print("Thanks for coming! Bye!")