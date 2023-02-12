from django.shortcuts import render, redirect
from .models import Animal
# Create your views here.


def index(request):
    template_name = 'animales/animal.html'
    context = {
        'title':'Animales',
        'animal_list': Animal.objects.all().order_by('-id'),
    }
    print('Listando...')

    return render(request,template_name, context )

def crear(request):
    nombre = 'Perro'
    descripcion = 'Es un perro de rasa Lassie'
    animal = Animal(nombre=nombre, descripcion=descripcion)
    animal.save()
    print('Creado...')

    return redirect('animales:index')