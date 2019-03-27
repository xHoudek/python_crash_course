my_pizzas = ['margherita', 'smoky the bandit', 'hawaiian']
your_pizzas = my_pizzas[:]

my_pizzas.append('meat lovers')
your_pizzas.append('porky fig')

print('My favorite pizzas are:')
for pizza in my_pizzas:
    print(pizza)

print('\nYour favorite pizzas are:')
for pizza in your_pizzas:
    print(pizza)
