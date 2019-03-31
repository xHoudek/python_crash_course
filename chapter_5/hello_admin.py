users = ('admin', 'nicole', 'noah', 'chris', 'amelia')

if users:
    for user in users:
        if user == 'admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print('Hello %s, thank you for logging in today' % user.title())
else:
    print('We need to find some users!')