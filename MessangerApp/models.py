from django.db import models

import time

class Message(models.Model):
    id=models.CharField(primary_key=True, max_length=100)
    message=models.CharField(max_length=500,null=True)
    key=models.CharField(max_length=100,null=True)
    user=models.EmailField(null=True)
    
    @staticmethod
    def genrateID(userInfo):
        return str(userInfo.id)+str(time.time()).replace(".","")

class UserInfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=15,null=True)
    msgs=models.ForeignKey('Message', on_delete=models.DO_NOTHING, null=True)