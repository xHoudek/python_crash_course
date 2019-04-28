filename = 'chapter_10/learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

message = ''
for line in lines:
    message += line

new_message = message.replace('Python', 'Java')

print(new_message)