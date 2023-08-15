from django.shortcuts import render
from . models import Finch

# Define view functions here

def home(request):
    #pass request object first
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    #search the db for ALL of the cats
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

    #match the html template path for the 2nd arg
    return render(request, 'finches/detail.html', {'finch' : finch})