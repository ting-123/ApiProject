from django.db import models
from Api_app import *

# Create your models here.
class DB_notice(models.Model):
    content = models.CharField(max_length=100,null=True,blank=True,default='')
    def __str__(self):
        return self.content