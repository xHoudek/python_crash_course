class Restaurant():
    """a simple attempt to model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """initializes restaurant_name and cuisine_type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """prints the name and cuisine type of the restaurant"""
        print(
            self.restaurant_name.title() + ' is a restaurant that serves '
            + self.cuisine_type.title()
        )

    def open_restaurant(self):
        """simulates opening the restaurant"""
        print(self.restaurant_name.title() + ' is now open')

    def show_number_served(self):
        """prints the amount of people that have been served"""
        print('Number served: ' + str(self.number_served))

    def set_number_served(self, customers):
        """set the number or customers served to the given value"""
        self.number_served = customers

    def increment_number_served(self, customers):
        self.number_served += customers


class IceCreamStand(Restaurant):
    """a representation of a restaurant, specifically an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type, number_served, flavors):
        """
        initialize attributes of the parent class
        then initialize attributes specific to an ice cream stand
        """
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self, flavors):
        print('Available flavors:')
        for flavor in flavors:
            print(flavor.title())
