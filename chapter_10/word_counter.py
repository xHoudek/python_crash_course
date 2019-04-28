def count_words(path, filename):
    """count the approximate number of words in a file"""
    try:
        with open(path + filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print('the file ' + filename + ' has about ' + str(num_words) + ' words')

path = 'chapter_10/'
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames:
    count_words(path, filename)