def describe_pet(animal_type, pet_name):
    """Display information about your pet!"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet(user_animal_type, user_pet_name)

def pet_information():
    """Ask for your pet name and type of animal an pass the argument though the describe pets function"""
    user_animal_type = input("Tell me what kind of pet do you have? ")
    user_pet_name = input("What's your pets name? ")
    describe_pet(user_animal_type, user_pet_name)

#pet_information()
#pet_information()

def pet_polling():
    """Enter various time information about several pets"""
    amount_pets = int(input("How many pets do you have? "))
    while amount_pets > 0:
        pet_information()
        amount_pets -= 1

pet_polling()