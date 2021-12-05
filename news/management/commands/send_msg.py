from django.core.mail import send_mail
from django.template import loader

send_mail(
    'Subject here',
    'Here is the message.',
    'ddddnews111@gmail.com',
    ['dospan2001@gmail.com'],
    fail_silently=False,
)
