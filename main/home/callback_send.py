from django.core.mail import send_mail

from home.models import BaseSettings

EMAIL_FROM = "info@xn----7sbah6bllcobpj.xn--p1ai"

try:
  email_clients = BaseSettings.objects.get().email
  print(email_clients)
except:
  email_clients = 'saniagolovanev@gmail.com'
  print(email_clients)
  

def email_callback(messages, title):
  send_mail(
    title,
    messages,
    EMAIL_FROM,
    email_clients.split(','),
    fail_silently=False,
  )