from django.db import models

class user_profile(models.Model):
    user_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gst_no = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12)
    pancard = models.CharField(max_length=9)
    address = models.TextField()
    
    
