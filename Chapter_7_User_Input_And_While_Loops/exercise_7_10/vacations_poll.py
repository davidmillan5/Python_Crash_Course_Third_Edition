responses = {}

# Set a Flag
polling_active = True

while polling_active:
    # Prompt about your dream vacations
    dream_vacation = input("\n If you could visit your dream country in the world, where would you go? ")
    dream_city = input("Which cities would you like to visit?")

    #Store the response
    responses[dream_vacation] = dream_city

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like another person to respond?  (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show Results.
print("\n------- Poll Results --------")
for dream_vacation, dream_city in responses.items():
    print(f"My dream vacation destination to visit is {dream_vacation} and I'll love to go to {dream_city}.")

