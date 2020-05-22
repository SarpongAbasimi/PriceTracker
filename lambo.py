from bs4 import BeautifulSoup
from email_client import EmailProvider
import requests
import logging

class Lambo(object):

  def __init__(self, beautiful_soup = BeautifulSoup, budget = 1000,  email_client = EmailProvider):
    self.soup =  beautiful_soup
    self.budget = budget
    self.email_client = email_client

  def get(self, url):
    try:
      request = requests.get(url)
      if(request.status_code == 200):
        content = self.soup(request.content, features='html.parser')
        return content
    except:
      logging.debug('Something went wrong')
  
  def prices(self, url, tag=None, css_class=None):
    try:
      list_of_price = []
      nodes = self.get(url).find_all(tag, class_= css_class)

      for cars in nodes:
        for prices in cars.stripped_strings:
          list_of_price.append(prices[1:].replace(',', ''))
      return list_of_price[1: -1]
    except:
      logging.debug(f'There was an error please chek that the {url}, {tag} and {css_class} are correct')

  def can_afford_lambo(self, url, tag=None, css_class=None):
    filter_lambo_prices = lambda x : int(float(x)) < self.budget
    lucky_day = list(filter(filter_lambo_prices, self.prices(url, tag, css_class)))

    if(len(lucky_day) < 1):
      print("""
    No Lambo mate! 
    You need to work hard and get your finances up else forget about Lambo buying a Lambo.""")
    else:
      print(f'It is your Lucky day man, You can finally buy a Lambo. Lambo Prices are {lucky_day}')
      self.email_client.send_email(lucky_day, url)

  