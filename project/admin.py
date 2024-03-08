from django.contrib import admin
from .models import Company, Employee, Question, Result

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Question)
admin.site.register(Result)
