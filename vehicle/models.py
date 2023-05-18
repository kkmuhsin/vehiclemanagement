from django.db import models

class vehicles(models.Model):
    vehicle_no=models.CharField(max_length=50)
    vechicle_type=models.CharField(max_length=100)
    vechicle_model=models.CharField(max_length=100)
    discription=models.CharField(max_length=200)
    
   


