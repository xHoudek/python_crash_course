favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python,'
}

poll = ['phil', 'rose', 'edward', 'karen']

for person in poll:
    if person in favorite_languages.keys():
        print('Thank you for responding to the poll!')
    else:
        print('Please take the poll!')