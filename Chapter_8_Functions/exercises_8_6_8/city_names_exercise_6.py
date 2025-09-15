def city_country(city,country):
    """Function to return a string formatted about a city and a country"""
    city_country_formatted = f"{city}, {country}"
    return city_country_formatted.title()

while True:
    print("\nPlease tell me the name of a city:")
    print("\n Please tell me the name of the country from that city:")
    print("(enter 'q' at anytime to quit))")

    city_name = input("City name: ")
    if city_name == 'q':
        break

    country_name = input("Country name: ")
    if country_name == 'q':
        break

    formatted_country_city_name = city_country(city_name, country_name)
    print(f"{formatted_country_city_name}")