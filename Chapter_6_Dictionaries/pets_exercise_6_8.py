pets = [
    {'animal': 'dog', 'owner': 'Sarah'},
    {'animal': 'cat', 'owner': 'Mike'},
    {'animal': 'hamster', 'owner': 'Jessica'},
    {'animal': 'bird', 'owner': 'Carlos'},
    {'animal': 'fish', 'owner': 'Emma'},
    {'animal': 'rabbit', 'owner': 'David'},
    {'animal': 'turtle', 'owner': 'Lisa'},
    {'animal': 'snake', 'owner': 'Alex'},
]

for registry in pets:
    animal = registry['animal']
    owner = registry['owner']
    print(f"{owner.title()} owns a {animal.title()}.")