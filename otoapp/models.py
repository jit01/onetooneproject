from django.db import models

class student(models.Model):
    sname = models.CharField(max_length=20)
    sloc = models.CharField(max_length=20)
    sage = models.IntegerField()
    def __str__(self):
        return self.sname

class course(models.Model):
    cid_id = models.OneToOneField(student, on_delete=models.DO_NOTHING)
    cname = models.CharField(max_length=20)
    fee = models.IntegerField()
    def __str__(self):
        return self.cname
# Create your models here.
