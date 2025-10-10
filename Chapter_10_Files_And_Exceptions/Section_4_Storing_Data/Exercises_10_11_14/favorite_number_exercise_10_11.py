from pathlib import Path
import json

def favorite_number():
    """Function to ask for the favorite number of a user"""
    favorite_number = int(input("Tell me your favorite number? "))
    path = Path('favorite_number.json')
    contents = json.dumps(favorite_number)
    path.write_text(contents)

def read_favorite_number():
    """Read the favorite number wrote in the .json file"""
    path = Path('favorite_number.json')
    contents = path.read_text()
    favorite_number = json.loads(contents)

    print(f"I know your favorite number! It's {favorite_number}")

favorite_number()

read_favorite_number()