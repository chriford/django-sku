from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

class User(AbstractBaseUser):
    first_name = models.CharField(
        _("First name"),
        max_length=200,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        _("Last name"),
        max_length=200,
        null=False,
        blank=False,
    )
    username = models.CharField(
        _("Username"),
        max_length=200,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        _("Email"),
        max_length=200,
        null=False,
        blank=False,
    )
    created = models.DateTimeField(
        _("date created"),
        editable=False,
        auto_now_add=True,
    )
    def __str__(self):
        if self.first_name & self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return self.username
    
    class Meta:
        ordering = ["created"]
        verbose_name = "User"
        verbose_name_plural = "Users"

