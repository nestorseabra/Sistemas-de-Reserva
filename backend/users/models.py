from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, default="Sem bio definida.")
    email = models.EmailField(unique=True, blank=False, null=False)
    nick_name = models.CharField(max_length=10, blank=False, null=False)

    def date(self):
        return self.date_joined 

    def new_email(self, new_email):
        if new_email != self.email:
            self.email = new_email
            self.save(update_fields=['email'])
            return True
        return False

    def new_bio(self, new_bio):
        self.bio = new_bio
        self.save(update_fields=['bio'])
        return True

    def update_password(self, new_password: str) -> bool:
        self.set_password(new_password)
        self.save(update_fields=['password'])
        return True

    def __str__(self):
        return f"{self.username} ({self.nick_name})"