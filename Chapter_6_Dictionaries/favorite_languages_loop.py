favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

### Looping Through All The Keys in A Dictionary

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")


    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")