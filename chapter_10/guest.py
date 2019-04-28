filename = 'chapter_10/guest.txt'

with open(filename, 'a') as file_object:
    name = input('what is your name? ')
    file_object.write(name + '\n')