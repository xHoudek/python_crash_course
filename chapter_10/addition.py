print('Enter two numbers and I will add them for you')
print("Press 'q' to quit")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break

    try:
        result = float(first_number) + float(second_number)
    except ValueError:
        print('Error: At least one input was not a number')
    else:
        print('Answer: ' + str(result))