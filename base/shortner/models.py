from django.db import models

import uuid
# Create your models here.

class Urldata(models.Model):
    url_id = models.UUIDField(primary_key=True,default = uuid.uuid4,unique = True)
    original_url = models.CharField(max_length = 255,null=False)
    short_id = models.CharField(max_length = 32,null=False)
    created_at = models.DateTimeField(auto_now_add = True)
    
