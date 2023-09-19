from django.db import models


class Receipe(models.Model):
    recepie_name=models.CharField(max_length=100)
    receipe_description=models.TextField()
    recepie_image=models.ImageField(upload_to='recepie/',null=True,default=None)
    
