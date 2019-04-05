dream_vacation = {}

while True:
    #poll someone
    name = input('\nWhat is your name?\n')
    place = input('\nIf you could visit one place in the world, where would you go?\n')
    
    #add name as key and place as value into the dictionary
    dream_vacation[name] = place

    #see if someone else is polling
    print('\nThank you, %s! Would you like to let someone else respond? (Y/N)' % name)
    repeat = input()
    if repeat.lower().startswith('y'):
        continue
    elif repeat.lower().startswith('n'):
        break

#print results
print('\nPOLL RESULTS')
for name, place in dream_vacation.items():
    print('%s would like to travel to %s.' % (name.title(), place))