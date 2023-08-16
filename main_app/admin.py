from django.contrib import admin

# Register your models here.
from .models import Finch, Feeding, Toy

#this will give us full CRUD operations in our admin app for the Cat table in our db
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Toy)