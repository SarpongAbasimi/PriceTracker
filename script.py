#!/usr/bin/env python
from model import Monitor

monitor = Monitor()
url = 'https://www.autotrader.co.uk/cars/lamborghini'

a = monitor.get_by_class(url, 'h2', 'atc-type-insignia')

print(a)
# request = monitor.get(url)

# cars = request.find_all('h2', class_='atc-type-insignia')

# list_of_price = []
# for car in cars:
#   for price in car.stripped_strings:
#     list_of_price.append(price[1:].replace(',', ''))

# prices = list_of_price[1:-1]

# find_car = lambda x : int(float(x)) < monitor.budget

# price_drop = list(filter(find_car, prices ))
# print(price_drop)

