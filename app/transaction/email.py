from django.core.mail import send_mail
from app.customer.models import Customer
from django.core import mail
from app.transaction.models import Transaction
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os

def SendMessage(transaction):
  CHOICES = {'b': 'borrow.html', 'l': 'lend.html', 'r': 'return.html', 'c': 'claim.html'}

  template = os.path.join('email', CHOICES[transaction.action])

  # open connections
  connection = mail.get_connection('django.core.mail.backends.console.EmailBackend')
  connection.open()  

  html_content = render_to_string(template, {'customer': transaction.customer, 'item': transaction.item, 'id': transaction.id})
  text_content = strip_tags(html_content)
 
  # create the email, and attach the HTML version as well.
  msg = EmailMultiAlternatives('Transaction Completed', text_content, 'from@example.com', [transaction.customer.email], connection=connection)
  msg.attach_alternative(html_content, "text/html")
  msg.send()

  # close connection
  connection.close()



