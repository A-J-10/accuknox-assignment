from django.db import models
class SampleModel(models.Model):
    name=models.CharField(max_length=100)
class AuditLog(models.Model):
    message=models.CharField(max_length=255)
class Rectangle:
    def __init__(self,length:int,width:int):
        self.length=length; self.width=width
    def __iter__(self):
        yield {'length':self.length}
        yield {'width':self.width}
