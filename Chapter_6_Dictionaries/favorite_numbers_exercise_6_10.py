favorite_numbers = {
    'estefania': [8, 5, 6, 20],
    'isabella': [16, 4, 5],
    'yrpelis': [4, 5, 16],
    'david': [5,8,20,16,4,18],
    'maria': [20,1]
}

for name, numbers in favorite_numbers.items():
    print(f"{name.title()} favorite numbers are: ")
    for number in numbers:
        print(f"\t - {number}")