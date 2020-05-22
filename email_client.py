import os
from smtplib import SMTP

class EmailProvider(object):

  def __init__(self, email_address, password, address_to_send_email_to):
    self.email_address = email_address
    self.password = password
    self.address_to_send_email_to = address_to_send_email_to

  
  def send_email(self, price, url_website):
    connection = SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.ehlo()

    connection.login(self.email_address, self.password)

    subject = 'You can now afford a Lambo'

    body = f"""
           Today is your Lucky day!
           Check the Lamborghini website {url_website}, because there is a Lamborghini avaliable for
           {price}
           """
    email_message = f'Subject: {subject}\n\n{body}'

    connection.sendmail(
      self.email_address,
      self.address_to_send_email_to,
      email_message
    )
    print('Email has been sent ..')
    connection.quit()