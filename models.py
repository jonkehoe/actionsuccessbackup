from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email

class Small_contact(models.Model):
    email_s = models.EmailField()
    message_s = models.TextField()

    def __str__(self):
        return self.email_s


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)















# class contactbackground()


# class portfoliobackground()