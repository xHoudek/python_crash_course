def word_counter(path, filename, word):
    try:
        with open(path + filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        count = contents.lower().count(word)
        print('Amount of times "' + word + '" appears in ' + filename + ': ' + str(count))

path = 'chapter_10/'
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
word = 'the'

for filename in filenames:
    word_counter(path, filename, word)