from collections import OrderedDict

glossary = OrderedDict()

glossary['list'] = 'a collection of items in a particular order'
glossary['tuple'] = 'a list of items that cannot change'
glossary['boolean expression'] = 'an expression that can be exaluated as True or False'
glossary['dictionary'] = 'a collection of key-value pairs'
glossary['string'] = 'a data type consisting of a series of characters'


for key, value in glossary.items():
    print(key +':\n' + value + '\n')