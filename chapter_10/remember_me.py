import json

#load the username, if it has been stored previously
#otherwise, prompt for the username and store it

def get_stored_username():
    """get stored username if available"""
    path = 'chapter_10/'
    filename = 'username.json'
    try:
        with open(path + filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """prompt for a new username"""
    path = 'chapter_10/'
    filename = 'username.json'
    username = input('What is your name? ')
    with open(path + filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """greet the user by name"""
    username = get_stored_username()
    if username:
        correct = input('Are you ' + username + '? (y/n) ' )
        if correct.lower() == 'y':
            print('Welcome back, ' + username + '!')
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')        

greet_user()