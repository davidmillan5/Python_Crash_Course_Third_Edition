favorite_places = {
    'estefania': ['tayrona', 'san andres', 'santa marta'],
    'leonardo': ['florencia', 'roma', 'vinci'],
    'torben': ['hamburg', 'klagenfurt', 'medellin'],
    'gabriela': ['caracas', 'san diego', 'medellin'],
}

for name, cities in favorite_places.items():
    print(f"{name.title()} loves to go to:")
    for city in cities:
        print(f"\t - {city.title()}.")