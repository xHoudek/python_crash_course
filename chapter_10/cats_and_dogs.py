def read_file(path, filename):
    try:
        with open(path + filename) as f_obj:
            contents = f_obj.readlines()
    except FileNotFoundError:
        pass
    else:
        print(filename + ':')
        for line in contents:
            print(line.strip())

path = 'chapter_10/'
cats = 'cats.txt'
dogs = 'dogs.txt'

read_file(path, cats)
print()
read_file(path, dogs)