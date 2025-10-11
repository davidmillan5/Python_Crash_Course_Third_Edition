from city_functions import city_country

def test_city_country():
    """Function test to verify that the name Santiago, Chile. is printed correctly"""
    formatted_city = city_country('santiago','chile')
    assert formatted_city == 'Santiago, Chile.'


def test_city_country_population():
    """Function test to verify that the name Santiago, Chile - population 5000000. is printed correctly"""
    formatted_city = city_country('santiago', 'chile', 5000000)
    assert formatted_city == 'Santiago, Chile - Population 5000000.'