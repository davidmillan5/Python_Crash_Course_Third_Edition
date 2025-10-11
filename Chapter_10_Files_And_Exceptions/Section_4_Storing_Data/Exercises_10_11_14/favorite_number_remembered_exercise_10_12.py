from pathlib import Path
import json

def favorite_number():
    """Function to ask for the favorite number of a user"""
    path = Path('favorite_number.json')
    favorite_number = favorite_number_exists(path)
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}")
    else:
        favorite_number = int(input("Tell me your favorite number? "))
        contents = json.dumps(favorite_number)
        path.write_text(contents)
        print(f"I will remember your favorite number when you come back!")


def read_favorite_number():
    """Read the favorite number wrote in the .json file"""
    path = Path('favorite_number.json')
    contents = path.read_text()
    favorite_number = json.loads(contents)

    print(f"I know your favorite number! It's {favorite_number}")


def favorite_number_exists(path):
    """Verify if the favorite number already exists in the .json archive"""

    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return None


favorite_number()