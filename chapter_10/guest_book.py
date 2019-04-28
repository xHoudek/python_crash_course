filename = 'chapter_10/guest_book.txt'

while True:
    with open(filename, 'a') as file_object:
        name = input('What is your name? (type exit to exit) ')
        if name.lower() == 'exit':
            break
        else:
            print('Hello, ' + name.title() + '!')
            file_object.write(name.title() + '\n')