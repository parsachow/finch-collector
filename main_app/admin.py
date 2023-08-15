from django.contrib import admin

# Register your models here.
from .models import Finch

#this will give us full CRUD operations in our admin app for the Cat table in our db
admin.site.register(Finch)