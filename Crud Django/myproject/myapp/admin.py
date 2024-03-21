from django.contrib import admin
from .models import person

# Register your models here.


class personAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
  
admin.site.register(person, personAdmin)
