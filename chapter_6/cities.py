cities = {
    'Stockholm': {
        'Country': 'Sweden',
        'Population': '962,000',
        'Fact': 'first Nobel Prizes awarded here in 1901'
    },
    'Minneapolis': {
        'Country': 'United States of America',
        'Population': '422,000',
        'Fact': 'Home to the longest skyway system in the world'
    },
    'Tokyo': {
        'Country': 'Japan',
        'Population': '9,200,000',
        'Fact': 'Largest metropolitan area in the world'
    }
}

for city, information in cities.items():
    print(city + ':')
    for key, value in information.items():
        print(key + ': ' + value)
    print()