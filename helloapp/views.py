from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
	text = "<h1><font color='blue'>Welcome to my hello app !</font></h1>"
	return HttpResponse(text)

def abc(request):
	text = "<h3><font color='green'>Welcome to Django !</font></h3>"
	return HttpResponse(text)

# ------------------

from helloapp.models import Dreamreal

def crudops(request):
	#Creating an entry
	dreamreal = Dreamreal(
		website = "www.polo.com",
		mail = "sorex@polo.com",
		name = "sorex",
		phonenumber = "002376970"
	)
	dreamreal.save()
	
	#Read ALL entries
	objects = Dreamreal.objects.all()
	res ='Printing all Dreamreal entries in the DB : <br>'
	for elt in objects:
		res += elt.name+"<br>"
		
	#Read a specific entry:
	sorex = Dreamreal.objects.get(name = "sorex")
	res += 'Printing One entry <br>'
	res += sorex.name
	
	#Delete an entry
	res += '<br> Deleting an entry <br>'
	sorex.delete()
	
	#Update
	dreamreal = Dreamreal(
		website = "www.polo.com",
		mail = "sorex@polo.com",
		name = "sorex",
		phonenumber = "002376970"
	)
	dreamreal.save()
	res += 'Updating entry<br>'
	
	dreamreal = Dreamreal.objects.get(name = 'sorex')
	dreamreal.name = 'thierry'
	dreamreal.save()
	
	return HttpResponse(res)
