def describe_city(city_name, country_name):
    """Simple function to print a sentence with a city name from a specific country"""
    print(f"{city_name.title()} is in {country_name.title()}.")

def input_city_information():
    """Function to capture the information needed to execute the function describe_city()"""
    input_city = input("Please enter the name of a city you will like to visit in the future: \n")
    input_country = input("Please enter the country of the city you mentioned.\n ")

    describe_city(input_city, input_country)

def cities_polling():
    """Function to execute the city polling n number of times"""

    cities_quantity = int(input("How many cities and countries would you like to visit? \n"))
    dream_cities = True

    while dream_cities:
        if cities_quantity > 0:
            input_city_information()
            cities_quantity -= 1
        if cities_quantity == 0:
            dream_cities = False
            print("Thanks for your time")



cities_polling()
