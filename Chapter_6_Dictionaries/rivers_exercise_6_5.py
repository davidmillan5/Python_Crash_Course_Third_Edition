rivers = {
    'nile': 'egypt',
    'congo': 'congo',
    'zambezi': 'namibia',
    'yangtze': 'china',
    'mekong': 'china',
    'brahmaputra': 'india',
    'volga': 'russia',
    'danube': 'germany',
    'mississippi': 'united states',
    'amazon': 'brazil',
    'plata': 'argentina',
    }

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

print("List of names of some of the most famous rivers in the world: \n")
for river in rivers.keys():
    print(f"{river.title()}")

print("List of some countries with the most famous rivers in the world: \n")
for country in rivers.values():
    print(f"{country.title()}")