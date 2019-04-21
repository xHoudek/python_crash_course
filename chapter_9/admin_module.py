from user_module import User

class Privileges():
    """creates a set of privileges"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self, privileges):
        print('Privileges:')
        for privilege in privileges:
            print(privilege)


class Admin(User):
    """creates a simple admin profile"""

    def __init__(
        self, first_name, last_name, age, location, username, privileges, login_attempts=0
        ):
        super().__init__(first_name, last_name, age, location, username)
        self.login_attempts = login_attempts
        self.privileges = Privileges(privileges)