from django.db import models

# Create your models here.
class Student(models.Model):
    sname = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    sem = models.IntegerField()
    
class Dreamreal(models.Model):
    website = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()
    
    def __str__(self):
        return '{}:{}, {}-{}'.format(self.id, self.name, str(self.phonenumber), self.mail, self.website)

    class Meta:
        db_table = "dreamreal"
