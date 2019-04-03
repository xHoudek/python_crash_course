favorite_places = {
    'Jon': ['Winterfell', 'The Wall'],
    'Cersei': ["King's Landing"],
    'Varys': ["King's Landing", 'Essos', 'Dragonstone']
}

for person, places in favorite_places.items():
    print(person + ':')
    for place in places:
        print(place)
    print()