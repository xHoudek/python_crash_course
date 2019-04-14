def make_car(make, model, **car_info):
    #Build a dictionary containing everything we know about the car
    car = {}
    car['make'] = make
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

my_car = make_car('honda', 'civic', hybrid=True, year='2009', color='black')

print(my_car)