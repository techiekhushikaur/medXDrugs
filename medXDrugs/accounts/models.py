from django.db import models
from django.contrib.auth.models import User
# Create your models here.
COLOR_CHOICES = (
    ('pending','PENDING'),
    ('ok', 'APPROVED'),
    ('no','NOT ALLOWED'),
   
)

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)
       
    def __str__(self):
        return "profile {}".format(self.user.username)

class NGO(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        approved = models.CharField(max_length=8, choices=COLOR_CHOICES, default='pending')

        def __str__(self):
         return "NGO {}".format(self.user.username)
       
