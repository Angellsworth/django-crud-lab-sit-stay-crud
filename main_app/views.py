from django.shortcuts import render
from .models import Dog
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Home page view
def home(request):
    return render(request, 'home.html')

# About page view
def about(request):
    return render(request, 'about.html')

# Dogs index view
def dog_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })

# Dogs Detail view
def dog_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', { 'dog': dog })

# Create Class
class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']  # We won't allow changing the name

class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'