while True:
    topping = input("Please enter a pizza topping (type 'quit' to quit): ")
    if topping.lower() == 'quit':
        break
    else:
        print('I will add %s to the pizza!' % topping)