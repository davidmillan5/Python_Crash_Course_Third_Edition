messages = [
    "Hello there!",
    "How's it going?",
    "Nice weather today",
    "Running a bit late",
    "Thanks for waiting",
    "See you soon",
    "Take care",
    "Good luck!",
    "Almost done",
    "On my way",
]

sent_messages = []


def send_messages(messages, sent_messages):
    """
    This program prints messages and moves them into a new sent messages list
    """
    # Work with a copy so original isn't modified
    messages_copy = messages[:]
    counter = 1

    while messages_copy:
        message = messages_copy.pop(0)
        print(f"Message #{counter} {message.title()}")
        sent_messages.append(message)
        counter += 1

    print("Original messages:", messages)  # This will show all original values
    print("Remaining messages:", messages_copy)  # This will be empty
    print("Sent messages:", sent_messages)


send_messages(messages, sent_messages)