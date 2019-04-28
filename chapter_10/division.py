print("give me two numbers, and I'll divide them")
print("enter 'q' to quit")

while True:
    first_number = input('\nFirst number: ')
    if first_number.lower() == 'q':
        break
    second_number = input('Second number: ')
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)