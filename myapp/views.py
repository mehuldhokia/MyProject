from django.shortcuts import redirect, render
import datetime

from myapp.models import Student, Contact
# Create your views here.

from django.http import HttpResponse

from .forms import StudentForm, ContactForm

# ---------------- TEMPLATEs ----------------
def theme(request):
	return render(request, "theme.html")

def index(request):
	topic = "M.Sc. (I.T. & C.A.)"
	desc  = "Semester - 3rd (July-2021)"
	return render(request, "creative/home.html", {"topic":topic, "desc": desc})

def about(request):
	return render(request, "creative/about.html")

def services(request):
	return render(request, "creative/services.html")

def portfolio(request):
	return render(request, "creative/portfolio.html")

def contact(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			c = Contact(name = request.POST['name'], email = request.POST['email'], phone = request.POST['phone'], msg = request.POST['msg'])
			c.save()
			form = ContactForm()
			return render(request, "creative/contact.html", {'form':form,'flag':True})
	else:
		form = ContactForm()
		
	return render(request, "creative/contact.html", {'form':form})

# ---------------- CRUD OPERATIONS ----------------

def search_form(request):
	return render(request, 'creative/search_form.html')

def search(request):
	errors = []
	if 'name' in request.GET:
		name = request.GET['name']
		if name == "":
			errors.append('Field should not be empty !')
			# return HttpResponse('You submitted an empty form.')
		elif len(name) < 2:
			errors.append('Value less than 2 Characters not allowed !')
		else:
			data = Student.objects.filter(sname__icontains=name)
			return render(request, "creative/search_result.html", {'data': data, 'find': name})
	else:
		errors.append('Form element not available !')
			
	return render(request, "creative/search_form.html", {'errors': errors})


def studentData(request):
	s = Student.objects.all().order_by('-id')	# - for DESC Order
	return render(request, "creative/student_data.html", {'data': s})

def student_add_form(request):
	return render(request, 'creative/student_add_form.html')

def student_add(request):
	errors = []
	if (request.POST['sname'] == ""):
		errors.append('Student name should not be empty !')
	elif (request.POST['course'] == ""):
		errors.append('Course should not be empty !')
	elif (request.POST['sem'] == ""):
		errors.append('Semester should not be empty !')
	else:
		n = request.POST['sname']
		c = request.POST['course']
		s = request.POST['sem']
		# output = 'Data is submitted : {} {}-{}'.format(n,c,s)
		rec = Student.objects.create(sname = n, course = c, sem = s)
		return render(request, 'creative/student_add_form.html', {'flag':True})
	
	return render(request, "creative/student_add_form.html", {'errors': errors})

def student_edit(request, sid):
	studObj = Student.objects.get(id = sid)

	if request.method == "POST":
		errors = []
		if (request.POST['sname'] == ""):
			errors.append('Student name should not be empty !')
		elif (request.POST['course'] == ""):
			errors.append('Course should not be empty !')
		elif (request.POST['sem'] == ""):
			errors.append('Semester should not be empty !')
		else:
			studObj.sname 	= request.POST['sname']
			studObj.course 	= request.POST['course']
			studObj.sem 	= request.POST['sem']
			studObj.save()
			return redirect('student_data')
			# return render(request, 'creative/student_edit_form.html', {'flag':True})

	return render(request, 'creative/student_edit_form.html', {'rec':studObj})

def student_del(request, sid):
	studObj = Student.objects.get(id = sid)
	studObj.delete()
	return redirect('student_data')


# FORM Class
# Form submission in single method
def addForm(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			n = form.cleaned_data['sname']
			c = form.cleaned_data['course']
			s = form.cleaned_data['sem']
			
			rec = Student.objects.create(sname = n, course = c, sem = s)
			return HttpResponse("Data is Inserted")
	else:
		form = StudentForm()
		
	return render(request, "creative/about.html",{'form': form})

# --------------------------------------------

def show(request):
	text = "<h1><font color='orange'>Welcome to my first app !</font></h1>"
	return HttpResponse(text)

def home(request):
	name = "Ram Dasrath Sharma"
	color = "red"
	return render(request, "myapp/home.html", {"person_name" : name, "textcolor": color})

def displayDate(request):
	today = datetime.datetime.now().date()
	daysOfWeek = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
	return render(request, "myapp/displaydate.html", {"today" : today, "days_of_week" : daysOfWeek})
