from django.conf import settings
from django.core import mail
from django.core.mail import send_mail
from django.template.loader import render_to_string

def mailer(to, subject, template, context):
  # Load settings
  connection = mail.get_connection(settings.EMAIL_BACKEND)
  connection.open()

  # Generate template
  message = render_to_string(template, context)

  # Send email
  mail.EmailMessage(subject, message, settings.EMAIL_FROM, [to], connection=connection).send()
  connection.close()
