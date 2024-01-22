from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class User(AbstractUser):
    pass

class Urldata(models.Model):
    url_id = models.UUIDField(primary_key=True,default = uuid.uuid4,unique = True)
    original_url = models.CharField(max_length = 255,null=False)
    short_id = models.CharField(max_length = 32,null=False)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey('User',on_delete = models.CASCADE,related_name = 'creator')

    
