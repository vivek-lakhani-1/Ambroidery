from django.db import models

class user_register(models.Model):
    username = models.CharField(max_length=108,primary_key=True)
    password = models.CharField(max_length=108)
    firm = models.CharField(max_length=108)
    first_name = models.CharField(max_length=108)
    last_name = models.CharField(max_length=108)
    gst = models.CharField(max_length=108)
    pancard = models.CharField(max_length=9)
    address = models.TextField()
    
    

class partymodel(models.Model):
    username = models.CharField(max_length=108)
    firmname = models.CharField(max_length=108,primary_key=True)
    GST_no =  models.CharField(max_length=108)
    address =  models.CharField(max_length=108)
    mobile_no =  models.CharField(max_length=108)


class challanin(models.Model):
    
    to = models.CharField(max_length=108)
    from_to = models.CharField(max_length=108)
    Item_id = models.CharField(max_length=108)
    item_name = models.CharField(max_length=108)
    price = models.CharField(max_length=108)
    date = models.CharField(max_length=108)
    


class challandata(models.Model):
    challan_id = models.CharField(max_length=108)
    invoice = models.CharField(max_length=108)
    
    