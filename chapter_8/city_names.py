def city_country(city, country):
    format = city.title() + ', ' + country.title()
    return format

nyc = city_country('new york city', 'united states of america')
print(nyc)

oslo = city_country('oslo', 'norway')
print(oslo)

istanbul = city_country('istanbul', 'russia')
print(istanbul)