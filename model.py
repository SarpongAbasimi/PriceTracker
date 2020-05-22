from bs4 import BeautifulSoup
import requests

class Monitor(object):

  def __init__(self, beautiful_soup = BeautifulSoup, budget = 1000):
    self.soup =  beautiful_soup
    self.budget = budget

  def get(self, url):
    try:
      request = requests.get(url)
      if(request.status_code == 200):
        content = self.soup(request.content, features='html.parser')
        return content
    except:
      print('Something went wrong')
  
  def get_by_class(self, url, tag=None, css_class=None):
    try:
      list_of_price = []
      nodes = self.get(url).find_all(tag, class_= css_class)

      for cars in nodes:
        for prices in cars.stripped_strings:
          list_of_price.append(prices[1:].replace(',', '.'))
      return list_of_price[1: -1]
    except:
      print(f'There was an error please chek that the {url}, {tag} and {css_class} are correct')
