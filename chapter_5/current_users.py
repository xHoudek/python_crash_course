current_users = ['xhoudek', 'npotter726', 'ultralord9001',\
     'holyhandgrenade_42', 'tormund.giantsbane']
new_users = ['Winter_Is_Coming', 'swagman2000', 'xhoudek', 'avatar.aang', 'UltraLord9001']
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
        if user.lower() in current_users_lower:
            print('Username taken. Please select another')
        else:
            print('Username available!')
