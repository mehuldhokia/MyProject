from django.contrib import admin

from .models import Publisher, Author, Book, Student, Contact

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(Contact)