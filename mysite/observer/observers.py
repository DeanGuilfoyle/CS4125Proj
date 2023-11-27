from abc import ABC, abstractmethod
from django.core.mail import send_mail
from django.conf import settings

# Observer
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# ConcreteObserver
class EmailAlertObserver(Observer):
    def __init__(self, email_address):
        # Makes every observer store their own email address
        self.email_address = email_address

    def update(self, message: str):
        # Sends an email using Django's send_mail function
        send_mail(
            subject='New Sale Alert!',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email_address],
            fail_silently=False,
        )

