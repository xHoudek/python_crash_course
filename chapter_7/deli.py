sandwich_orders = [
    'BLT', 'Pastrami', 'Club', 'Cuban', 'Pastrami', 'Chicken Salad',
    'Pastrami', 'Grilled Cheese', 'Peanut Butter & Jelly'
]

finished_sandwiches = []

#Remove all instances of pastrami
print('The deli has run out of pastrami. Sorry for the inconvenience.\n')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

#Preparing the sandwiches
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('Making %s sandwich...' % sandwich)
    finished_sandwiches.append(sandwich)

#List all of the sandwiches that were made
print('\nThe following sandwiches are ready:')
for sandwich in finished_sandwiches:
    print(sandwich)