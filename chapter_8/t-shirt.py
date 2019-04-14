def make_shirt(size = 'large', text = 'I love Python'):
    print('A %s sized shirt with the text "%s" has been made.' % (size,text))

make_shirt('medium', 'Go Badgers')
make_shirt(size='large', text='Go Timberwolves')

make_shirt()
make_shirt('medium')
make_shirt(text='Go Vikings')