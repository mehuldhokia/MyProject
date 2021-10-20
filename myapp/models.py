from django.db import models

# Create your models here.
class Contact(models.Model):
	name 	= models.CharField(max_length=30)
	email 	= models.EmailField()
	phone	= models.CharField(max_length=15)
	msg		= models.CharField(max_length=255)

	def __str__(self):
		return self.name;

	class Meta:
		ordering = ['id']

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    def __str__ (self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__ (self):
        return '{} {}'.format(self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__ (self):
        return self.title


class Student(models.Model):
    sname = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    sem = models.IntegerField()
    
    # def __unicode__(self):
    #     return u"%d %s %s %d" % (self.id, self.sname, self.course, self.sem)
    
    def __str__ (self):
    #     data = "Student Name : " + self.sname
    #     data += " | Course : " + self.course
    #     data += " - Sem : " + str(self.sem)
        # return data
        return '{}:{}, {}-{}'.format(self.id, self.sname, self.course, str(self.sem))
    
    def display (self):
        return 'Roll {} : Student {}, Course {} - Sem {}'.format(self.id, self.sname, self.course, str(self.sem))

    class Meta:
        ordering = ['sname']