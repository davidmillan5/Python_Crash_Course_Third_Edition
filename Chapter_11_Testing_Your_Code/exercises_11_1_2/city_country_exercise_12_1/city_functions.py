def city_country(city, country, population=None):
    """Function that receive the name of a city and the country of the city printed."""
    if population:
        city_country_formatted = f"{city}, {country} - population {population}."
    else:
        city_country_formatted = f"{city}, {country}."
    return city_country_formatted.title()