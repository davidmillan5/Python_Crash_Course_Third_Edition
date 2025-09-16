def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


def input_users_into_list(user_list):
    """Input users into the users list"""
    print("----------  Users --------------")
    username = input("Enter name: \n")
    user_list.append(username)
    print(f"Current users: {user_list}")
    return user_list


def input_calling():
    """Function to define the amount of users on the list"""
    print("---------  Welcome to the user registry ----------")
    amount_users = int(input("How many users are you going to register? \n"))

    # Create the user list once here
    user_list = []

    while amount_users > 0:
        input_users_into_list(user_list)
        amount_users -= 1
    else:
        print("----- Thanks for the registry! -------")
        print(f"Final user list: {user_list}")
        print("Greeting all users:")
        greet_users(user_list)


input_calling()