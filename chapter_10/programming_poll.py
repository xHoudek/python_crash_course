filename = 'chapter_10/programming_poll_responses.txt'

while True:
    with open(filename, 'a') as file_object:
        response = input(' Why do you like programming? (type exit to exit) ')
        if response.lower() == 'exit':
            break
        else:
            print('Thank you for your response!')
            file_object.write(response + '\n')