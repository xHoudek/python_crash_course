favorite_numbers = {
    'Xander': [12],
    'Nicole': [666],
    'Chris': [4, 44],
    'Monty': [42, 7],
    'Henry': [1, 0, 10]
}

for name, numbers in favorite_numbers.items():
    print(name + ':')
    for number in numbers:
        print(number)
    print()