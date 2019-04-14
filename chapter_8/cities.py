def describe_city(city, country='Canada'):
    print('%s is in %s.' % (city.title(), country.title()))

describe_city('Toronto')
describe_city('Sydney', 'Australia')
describe_city('Nairobi', 'Kenya')