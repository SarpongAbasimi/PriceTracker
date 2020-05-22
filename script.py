#!/usr/bin/env python
import os
from lambo import Lambo
from email_client import EmailProvider
from dotenv import load_dotenv

load_dotenv()

email = os.getenv('Email')
password = os.getenv('Password')
address_to_send_email= os.getenv('EmailToSendTo')

client = EmailProvider(email_address=email,
                       password=password, 
                       address_to_send_email_to=address_to_send_email)

monitor = Lambo(budget=10, email_client=client)

url = 'https://www.autotrader.co.uk/cars/lamborghini'
monitor.can_afford_lambo(url, 'h2', 'atc-type-insignia')

# monitor.can_afford_lambo(url, 'h2', 'atc-type-insignia')
# a = monitor.prices(url, 'h2', 'atc-type-insignia')

# print(a)
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

