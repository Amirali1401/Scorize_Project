from django.contrib import admin

from .models import University , City , Country

# Register your models here.

admin.site.register(University)
admin.site.register(Country)
admin.site.register(City)