from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300, blank=True, null=True)
    last_name = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    bio = models.TextField(default="my bio")
    
    def __str__(self):
        return self.user.username
        
    

'''
update user profile - forms not woriking
set up cloudinary for profile images
set up reset password
set up forgot password
check out social auth
check out firbase auth
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#abstractuser
'''