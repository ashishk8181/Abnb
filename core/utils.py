from django.core.mail import send_mail
from django.core.mail import EmailMessage
from threading import Thread
from django.conf import settings


class AsyncCalls(Thread):
    def sendMail(self, to, subject, message):
        '''Here emailAddress will be list'''
        return send_mail(subject, message, settings.EMAIL_HOST_USER, to, fail_silently=False)

    