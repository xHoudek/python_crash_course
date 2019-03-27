snakes = ['ball python', 'dumerils boa', 'black milksnake', 'western hognose', 'garter snake', 'green tree python', 'rainbow boa', 'cornsnake']

print('The first three items in this list are:')
for snake in snakes[:3]:
    print(snake.title())

print('\nThree items from the middle of the list are:')
for snake in snakes[2:5]:
    print(snake.title())

print('\nThe last three items in the list are:')
for snake in snakes[-3:]:
    print(snake.title())