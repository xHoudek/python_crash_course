import json

def favorite_number():
    """tell user's favorite number"""
    number = guess_number()
    if number:
        print('I know your favorite number! It is ' + number)
    else:
        number_prompt()

def number_prompt():
    """prompts user for favorite number"""
    number = input('What is your favorite number? ')

    path = 'chapter_10/'
    filename = 'fav_number.json'
    with open(path + filename, 'w') as f_obj:
        json.dump(number, f_obj)
    print('I will remember that next time!')

def guess_number():
    """gets stored number if available"""    
    path = 'chapter_10/'
    filename = 'fav_number.json'
    try:
        with open(path + filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number
    
favorite_number()