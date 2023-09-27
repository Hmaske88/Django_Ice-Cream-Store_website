from django.db import models

# makemigrations --> create changes and save in a file
# migrate --> apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()
    
    def __str__(self):
        return self.name+" ("+self.email+")"