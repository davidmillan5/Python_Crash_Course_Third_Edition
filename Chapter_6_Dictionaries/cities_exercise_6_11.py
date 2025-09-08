cities = {
    'tokyo': {
        'country': 'Japan',
        'population': 37000000,
        'fact': 'Tokyo is the most populous metropolitan area in the world'
    },
    'paris': {
        'country': 'France', 
        'population': 2100000,
        'fact': 'Paris is known as the City of Light and has over 130 museums'
    },
    'sydney': {
        'country': 'Australia',
        'population': 5300000,
        'fact': 'Sydney Opera House has over 1 million roof tiles'
    }
}


for city, info in cities.items():
    print(f"{city.title()} facts: ")
    print(f"\tCountry Name: {info['country']}, "
          f"Population: {info['population']:,} people, "
          f"Fact: {info['fact']}")