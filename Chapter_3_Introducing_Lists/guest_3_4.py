guess_list = ['Bourdain', 'Leonardo', "Einstein", "Bohr", "Heissenberg", "Serrano", 'Gonzalez']

invitation_message = f"You are invited to the greatest event ever Mr.{guess_list[3]}."

print(guess_list)
print(invitation_message)

cant_come = guess_list.pop(3)
print(cant_come)

guess_list[3] = 'Platon'

print(guess_list)

invitation_message = f"You are invited to the greatest event ever Mr.{guess_list[3]}."
print(invitation_message)

found_bigger_table = f"Dear {guess_list[3]} we are happy to let you know that we found a bigger venue for our meeting"

print(found_bigger_table)

guess_list.insert(0,"Labatut")

guess_list.insert(4,"St. Brown")

guess_list.append("Gibbs")

print(guess_list)

smaller_venue = f"Mr. {guess_list[0]} sadly we have to tell you that the venue for the meeting can receive all of the invitated person."

print(smaller_venue)

guess_list.pop()

guess_list.pop()

del guess_list[-1]

print(guess_list)

del guess_list[-1]

print(guess_list)



