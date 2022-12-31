from django.db import models

# Create your models here.
class FirebaseConfig(models.Model):
     site = models.CharField(max_length=100,verbose_name="site")
     apiKey = models.CharField(max_length=100,verbose_name="apiKey")
     authDomain = models.CharField(max_length=250,verbose_name="authDomain")
     databaseURL = models.CharField(max_length=250,verbose_name="databaseURL")
     storageBucket = models.CharField(max_length=250,verbose_name="storageBucket")

     def __str__(self):
         return self.site
