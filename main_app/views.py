from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from . models import Finch, Toy
from . forms import FeedingForm

# Define view functions here

def home(request):
  #pass request object first
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finch_index(request):
  #search the db for ALL of the finches
  #objects can be replaced with any objects like toy/feeding
  finches = Finch.objects.all()

  #respond to the client, by injecting the finch list we found from the db into our finches/index.html template
  return render(request, 'finches/index.html', {
    #passing python data, 'finches' variable from above in this case
    'finches' : finches
  })

# finch_id needs to match the route in urls.py ---> path('finches/<int:finch_id>/'
def finch_detail(request, finch_id):

  # use our model to get the finch from the database with the same id as finch_id
  finch = Finch.objects.get(id=finch_id)

  #instantiate our Feeding Form 
  #create a form from our class
  feeding_form = FeedingForm()

  # to get the toys the bird has
  # finch_toys = finch.toys.all()

  # list of all the toys bird does not have
  # create a list of the toy ids the bird does have
  id_list = finch.toys.all().values_list('id')
  # query the toys model to find all of the toys that are not (exlcuded ) from the id_list
  toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
  # id__in is a field lookup in django (google, django model field lookups)
  # id is a property(key) on your MODEL, you can use any property/key you want for field lookup

  #match the html template path for the 2nd arg
  return render(request, 'finches/detail.html', {'finch' : finch, 'feeding_form' : feeding_form, 'toys' : toys_finch_doesnt_have,})


#CBV - class based view
class FinchCreate(CreateView): #FinchCreate inherits from createView
  
  #the one class attribute in every single cbv we work with
  model = Finch 

  #renders all fields that are defined in the Finch model. Fields will render in the order the model is made. If we want to change the order, we can list out each key in the order we want as a list [] ex; fields = ['name', 'description', 'age' ,'breed']
  # fields = '__all__' 
  fields = ['name', 'type', 'personality', 'color', 'age']

  # Or if you wanted to redirect to the index page success_url = '/finches'
  # success_url = '/finches/{finch_id}'


class FinchUpdate(UpdateView):
  model = Finch
  fields = ['type', 'personality', 'color', 'age']

class FinchDelete(DeleteView):
  model = Finch
  #a sucesses_url is mandatory for delete function (depending on our absolute url path) as the object we had created is now deleted. so the url needs to be redirected somewhere other than the id page as it doesn't exist anymore
  success_url = '/finches'

 #2nd argument is cat_id bc thats the route parameter in the URL
def add_feeding(request, finch_id): # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST) #request.POST = req.body in Express
    # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

#passing finch_id and toy_id as arguments from the params from assoc_toy URL
def assoc_toy(request, finch_id, toy_id):
  finch = Finch.objects.get(id=finch_id)
  finch.toys.add(toy_id)

  #we can also use this - 
  #Finch.objects.get(id=finch_id).toys.add(toy_id)

  return redirect('detail', finch_id=finch_id)


class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'