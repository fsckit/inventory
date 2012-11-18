from django.conf import settings
from django.core import mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def mailer(to, subject, template, context):
  # Load settings
  connection = mail.get_connection(settings.EMAIL_BACKEND)
  connection.open()

  # Generate template
  html_message = render_to_string(template, context)
  text_message = strip_tags(html_message)

  # Send email
  email = EmailMultiAlternatives(subject, text_message, settings.EMAIL_FROM, [to], connection=connection)
  email.attach_alternative(html_message, 'text/html')
  email.send()

  # Close connection
  connection.close()
