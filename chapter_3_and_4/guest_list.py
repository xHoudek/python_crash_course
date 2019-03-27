guests = ['Biggie Smalls', 'Tupac', 'Lil B', 'Kendrick Lamar']

#prints invites to all invited guests
for i in range(len(guests)):
    message = 'Dear %s, please come to my party.' % guests[i].title()
    print(message)

print('People invited: ' + str(len(guests)))

#someone couldn't make it to the party
cant_make_it = 'Tupac'
guests.remove(cant_make_it)
print('%s cannot make it :(' % cant_make_it)

print('People invited: ' + str(len(guests)))

#let's invite someone else
guests.append('Kanye West')

#print more invites
for i in range(len(guests)):
    message = 'Dear %s, please come to my party.' % guests[i].title()
    print(message)

print('People invited: ' + str(len(guests)))

#invite more people
print('I found a bigger dinner table!')

guests.insert(0, 'Chance the Rapper')
guests.insert(3, 'Young Thug')
guests.append('Pusha T')

#if it ain't broke don't fix it
for i in range(len(guests)):
    message = 'Dear %s, please come to my party.' % guests[i].title()
    print(message)

print('People invited: ' + str(len(guests)))

#oopsies
print("Table didn't come in time, now I can only invite two guests.")

uninvited = guests.pop(0)
print('Dear %s, I regret to inform you that your invitation to my party has been rescinded.' % uninvited)

uninvited = guests.pop(1)
print('Dear %s, I regret to inform you that your invitation to my party has been rescinded.' % uninvited)

uninvited = guests.pop(1)
print('Dear %s, I regret to inform you that your invitation to my party has been rescinded.' % uninvited)

uninvited = guests.pop(2)
print('Dear %s, I regret to inform you that your invitation to my party has been rescinded.' % uninvited)

uninvited = guests.pop(2)
print('Dear %s, I regret to inform you that your invitation to my party has been rescinded.' % uninvited)

#let the remaining two know they are still invited
for i in range(len(guests)):
    message = 'Dear %s, the nerds were uninvted but you can still come.' % guests[i]
    print(message)

print('People invited: ' + str(len(guests)))

#remove the last two names from list
del guests[0]
del guests[0]
print(guests)