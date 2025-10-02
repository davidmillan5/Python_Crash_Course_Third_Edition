import random


class Lottery:
    def __init__(self, pool):
        """
        Initialize the Lottery with a pool of numbers and letters.

        Args:
            pool: A list or tuple containing numbers and letters
        """
        self.pool = pool
        self.winning_combination = []

    def draw_winning_combination(self):
        """
        Randomly select 4 items from the pool as the winning combination.
        """
        self.winning_combination = random.sample(self.pool, 4)
        print(f"🎰 The winning combination is: {self.winning_combination}")
        print(f"Any ticket matching these 4 numbers or letters wins a prize!\n")
        return self.winning_combination

    def check_ticket(self, ticket):
        """
        Compare a ticket against the winning combination.

        Args:
            ticket: A list or tuple of 4 numbers/letters to check
        """
        if len(ticket) != 4:
            print("❌ Invalid ticket! Must contain exactly 4 items.\n")
            return False

        # Convert to sets for comparison (order doesn't matter)
        ticket_set = set(ticket)
        winning_set = set(self.winning_combination)

        if ticket_set == winning_set:
            print(f"🎉 WINNER! Your ticket {ticket} matches the winning combination!")
            print(f"Congratulations! You won the prize! 🏆\n")
            return True
        else:
            matches = ticket_set.intersection(winning_set)
            if matches:
                print(f"😊 Your ticket {ticket} matched {len(matches)} item(s): {matches}")
            else:
                print(f"😔 Your ticket {ticket} didn't match any items.")
            print("Keep trying! Better luck next time! 💪\n")
            return False