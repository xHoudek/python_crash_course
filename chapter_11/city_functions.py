def city_country(city, country, population=''):
    """generate a neatly formatted city name"""
    if population:
        location = city + ', ' + country + ' - population: ' + str(population)
    else:
        location = city + ', ' + country
    return location.title()