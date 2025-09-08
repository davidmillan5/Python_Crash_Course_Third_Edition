people = [
    {    
    'first_name': 'eren',
    'last_name': 'yaeger',
    'age': 14,
    'city': 'paradis'
    },
    {
    'first_name': 'edward',
    'last_name': 'elric',
    'age': 14,
    'city': 'resembool'  
    },
    {
    'first_name': 'rintaro',
    'last_name': 'okabe',
    'age': 17,
    'city': 'akihabara'
    },
          ]

for person in people:
    first_name = f"{person['first_name']}"
    last_name = f"{person['last_name']}"
    age = f"{person['age']}"
    city = f"{person['city']}"
    print(f"{first_name.title()} {last_name.title()} is {age} years old and "
          f"comes from the city of {city.title()}.")