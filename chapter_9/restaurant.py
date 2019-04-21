from restaurant_classes import Restaurant, IceCreamStand

great_dane = Restaurant('great dane', 'new american')
chilis = Restaurant('chilis', 'gross food')
laredos = Restaurant('laredos', 'mexican')

great_dane.describe_restaurant()
great_dane.open_restaurant()

chilis.describe_restaurant()
laredos.describe_restaurant()


restaurant = Restaurant('food place', 'food')
restaurant.show_number_served()

restaurant.number_served = 10
restaurant.show_number_served()

restaurant.set_number_served(50)
restaurant.show_number_served()

restaurant.increment_number_served(5)
restaurant.show_number_served()


michaels_flavors = ['vanilla', 'chocolate', 'cookies & cream', 'cookie dough', 'superman']
michaels = IceCreamStand("michael's", 'ice cream', 20, michaels_flavors)

michaels.display_flavors(michaels_flavors)