magicians = ['houdini', 'david blaine', 'jay']

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append('The great ' +  magician.title())
    return great_magicians


show_magicians(magicians)
great_magicians = make_great(magicians)
show_magicians(great_magicians)