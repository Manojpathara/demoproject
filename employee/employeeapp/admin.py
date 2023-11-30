from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id','name','address','age']
    ordering =('name',)
    search_fields = ('name','address')
    
admin.site.register(Employee,EmployeeAdmin)  