# Import the Lottery class from the lottery module
# Assuming your class file is named 'lottery.py'
from lottery import Lottery

# Create a pool of 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Create an instance of the Lottery class
my_lottery = Lottery(lottery_pool)

# Draw the winning combination
print("=" * 60)
print("WELCOME TO THE LOTTERY!")
print("=" * 60)
my_lottery.draw_winning_combination()

# Method 1: Create your own ticket and check it
print("Method 1: Checking a custom ticket")
print("-" * 60)
my_ticket = [5, 'A', 8, 'C']
my_lottery.check_ticket(my_ticket)

# Method 2: Keep playing until you win!
print("\nMethod 2: Playing until we win!")
print("-" * 60)
attempts = 0
won = False

while not won:
    attempts += 1
    # Generate a random ticket
    import random

    random_ticket = random.sample(lottery_pool, 4)

    print(f"Attempt {attempts}: Trying ticket {random_ticket}")
    won = my_lottery.check_ticket(random_ticket)

print(f"🎊 It took {attempts} attempts to win!")

# Method 3: Guaranteed win - use the winning combination
print("\n" + "=" * 60)
print("Method 3: Guaranteed win using the winning combination")
print("-" * 60)
winning_ticket = my_lottery.winning_combination.copy()
my_lottery.check_ticket(winning_ticket)