places_to_visit = ['Stockholm', 'Toronto', 'San Francisco', 'Auckland', 'Seattle']
print(places_to_visit)

#alphabetical order
print(sorted(places_to_visit))

#list is still in original order
print(places_to_visit)

#reverse alphabetical order
print(sorted(places_to_visit, reverse=True))

#list is still in original order
print(places_to_visit)

#reverse order of list
places_to_visit.reverse()
print(places_to_visit)

#put list back to original order
places_to_visit.reverse()
print(places_to_visit)

#put list in alphabetical order (permanently)
places_to_visit.sort()
print(places_to_visit)

#put list in reverse alphabetical order (permanently)
places_to_visit.sort(reverse=True)
print(places_to_visit)