
from django.db import models  

from django.contrib.auth.models import User 

# Create your models here. 

 

class Profil(models.Model): 

    user=models.OneToOneField(User,on_delete=models.CASCADE) 

    avatar=models.ImageField(upload_to="profil/avatar/",null=True,blank=True) 

    premium=models.BooleanField(default=False) 

    tel1=models.CharField(max_length=12,null=True,blank=True) 

    tel2=models.CharField(max_length=12,null=True,blank=True) 

    tel3=models.CharField(max_length=12,null=True,blank=True) 

 

    def __str__(self) -> str: 

        return self.user.username 

