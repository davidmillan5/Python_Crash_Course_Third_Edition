user_animal_type = input("Tell me what kind of pet do you have? ")
user_pet_name = input("What's your pets name? ")

def describe_pet(animal_type, pet_name):
    """Display information about your pet!"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(user_animal_type, user_pet_name)