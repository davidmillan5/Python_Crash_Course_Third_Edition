from pathlib import Path

guest = input("Enter your name: \n")

path = Path("guest.txt")
path.write_text(guest)

