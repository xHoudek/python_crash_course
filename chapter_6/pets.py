casanova = {'name': 'Casanova', 'type': 'snake', 'owner': 'Xander and Nicole'}
annie = {'name': 'Annie', 'type': 'snake', 'owner': 'Xander and Nicole'}
bear = {'name': 'Bear', 'type': 'cat', 'owner': 'Ben and Jolan'}
molly = {'name': 'Molly', 'type': 'dog', 'owner': 'Mom and Dad'}
gibson = {'name': 'Gibson', 'type': 'dog', 'owner': 'Mom and Dad'}

pets = [casanova, annie, bear, molly, gibson]

for pet in pets:
    for key, value in pet.items():
        print(key.title() + ': ' + value)
    print()