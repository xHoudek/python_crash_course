active = True
while active:
    age = int(input("Enter your age (type '999' to quit): "))
    if age == 999:
        active = False
    else:
        if age < 3:
            price = 0
        elif 3 <= age <= 12:
            price = 10
        elif age > 12:
            price = 15
        print('The cost of your movie ticket is $' + str(price) + '.')