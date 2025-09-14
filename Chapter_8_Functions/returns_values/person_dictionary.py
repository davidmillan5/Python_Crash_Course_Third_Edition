def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person."""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

def input_person():
    """Input data to create a person dictionary"""
    input_first_name = input("Please enter your name: \n")
    input_last_name = input("Please enter your last name: \n")
    input_age = int(input("Please enter your age: \n"))

    person = build_person(input_first_name, input_last_name, input_age)
    print(person)

input_person()