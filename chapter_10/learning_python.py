filename = 'chapter_10/learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

with open(filename) as file_object:
    lines = file_object.readlines()

    for line in lines:
        print(line)

with open(filename) as file_object:
    lines = file_object.readlines()
    
learning_string = ''
for line in lines:
    learning_string += line

print(learning_string)