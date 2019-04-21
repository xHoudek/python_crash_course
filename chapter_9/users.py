from user_module import User
from admin_module import Admin, Privileges


xhoudek = User('xander', 'houdek', 23, 'madison, wisconsin', 'xhoudek')
npotter = User('nicole', 'potter', 22, 'madison, wisconsin', 'npotter')
bran = User('bran', 'stark', 17, 'winterfell', '3_eyed_raven')

xhoudek.describe_user()
xhoudek.greet_user()

npotter.describe_user()
npotter.greet_user()

bran.describe_user()
bran.greet_user()


xhoudek.increment_login_attempts()
print(xhoudek.login_attempts)

xhoudek.reset_login_attempts()
print(xhoudek.login_attempts)


admin_privileges = ['can add post', 'can delete post', 'can ban user']
admin = Admin('xander', 'houdek', 23, 'Madison', 'xhoudek', admin_privileges)

admin.privileges.show_privileges(admin_privileges)