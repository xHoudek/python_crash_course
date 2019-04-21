class User():
    """creates a simple user profile"""

    def __init__(self, first_name, last_name, age, location, username, login_attempts=0):
        """initializes user information as attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.username = username
        self.login_attempts = login_attempts

    def describe_user(self):
        print('First name: ' + self.first_name.title())
        print('Last name: ' + self.last_name.title())
        print('Username: ' + self.username)
        print('Age: ' + str(self.age))
        print('Location: ' + self.location.title())

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + '!')    

    def increment_login_attempts(self):
        """increases amount of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets amount of login attempts to 0"""
        self.login_attempts = 0