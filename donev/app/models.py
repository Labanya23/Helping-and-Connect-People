from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length = 15,null = True)
    address = models.CharField(max_length = 300,null=True)
    userpic = models.ImageField(upload_to='donor',null=True,blank=True)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

# Create your models here.
