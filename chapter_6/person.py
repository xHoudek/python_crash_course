xander = {'first_name': 'Xander', 'last_name': 'Houdek', 'age': 23, 'city': 'Madison, WI'}

print(xander['first_name'])
print(xander['last_name'])
print(xander['age'])
print(xander['city'])
print()

nicole = {'first_name': 'Nicole', 'last_name': 'Potter', 'age': 22, 'city': 'Madison, WI'}
noah = {'first_name': 'Noah', 'last_name': 'Houdek', 'age': 20, 'city': 'New Richmond, WI'}

people = [xander, nicole, noah]

for person in people:
    for key, value in person.items():
        print(key.title() + ': ' + str(value))
    print()