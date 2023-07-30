from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name




class Person(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    mail=models.EmailField(max_length=254)
    address=models.TextField()
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    accountType=models.CharField(max_length=100, blank=True, null=True)
    materials=models.CharField(max_length=50)


    def __str__(self):
        return self.name

