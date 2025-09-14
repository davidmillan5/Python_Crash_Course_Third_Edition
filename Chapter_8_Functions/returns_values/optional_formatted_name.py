def get_formatted_name(first_name, last_name, middle_name =''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


def fullname_input():
    """Input the first name and last name of the users"""
    user_name = input("Please enter your name: \n")
    user_middle_name = input("Please enter your middle name: \n")
    user_last_name = input("Please enter your last name: \n")

    username = get_formatted_name(user_name, user_last_name, user_middle_name)
    print(username)

fullname_input()