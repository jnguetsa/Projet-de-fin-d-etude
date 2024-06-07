from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class PharmaUser(AbstractUser):
    
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    pharmaciens= models.BooleanField(default= False)
    gestionnaires= models.BooleanField(default= False)
    personne= models.BooleanField(default= True)
    
    def __str__(self):
        return self.username