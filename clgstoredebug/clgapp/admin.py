from django.contrib import admin
from . models import student,department,course,purpose,material

# Register your models here.
admin.site.register(student)
admin.site.register(department)
admin.site.register(course)
admin.site.register(purpose)
admin.site.register(material)