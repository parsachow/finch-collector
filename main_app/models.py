from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.
#Every time we add a model, Add it to the ADMIN.PY file and makemigrations/migrate
# all our models will inherit from djangos models.Model class
# the Model class gives our model all the methods to perform CRUD operations on a table in the database!


#Toy Class goes on the top of Finch Class bc it has to be available first, for Finch Class to access it in the first place 
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    # define the column names, and the dataypes(field types in django) in each row 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    personality = models.TextField(max_length=250)
    color = models.CharField(max_length=100)
    age = models.IntegerField()
    # Create a M:M relationship with Toy
    # toys is the Related Manager
    toys = models.ManyToManyField(Toy)

    def __str__(self):
      return f'{self.name} ({self.id})'

    def get_absolute_url(self):
    #make sure the kwargs and params match for the url
      return reverse('detail', kwargs={'finch_id': self.id})
    
    def fed_for_today(self):
       return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)
    

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

class Feeding(models.Model):
    date = models.DateField()
    # choices, select menu on the form
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    # create a finch_id FK, it will automatically add the _id to the key name 
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    # on_Delete says if we delete a finch, delete ALL the feedings of that particular finch

    def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
       ordering = ['-date']