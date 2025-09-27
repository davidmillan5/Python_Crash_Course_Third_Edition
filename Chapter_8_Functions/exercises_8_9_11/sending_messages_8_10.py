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
    counter = 1
    while messages:
        message = messages.pop(0)  # Always pop from index 0
        print(f"Message #{counter} {message.title()}")
        sent_messages.append(message)
        counter += 1

    print("Remaining messages:", messages)
    print("Sent messages:", sent_messages)


send_messages(messages, sent_messages)