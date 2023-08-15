from django.db import models

# Create your models here.

# Create your models here.
# all our models will inherit from djangos models.Model class
# the Model class gives our model all the methods to perform CRUD operations on a table in the database!
class Finch(models.Model):
    # define the column names, and the dataypes(field types in django) in each row 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    personality = models.TextField(max_length=250)
    color = models.CharField(max_length=100)
    age = models.IntegerField()