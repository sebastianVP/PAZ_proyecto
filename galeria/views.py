from django.shortcuts import render

# Create your views here.
def ver_imagenes(request):
    imagenes = [
        'galeria/f_001.jpeg',
        'galeria/f_002.jpeg',
        'galeria/f_003.jpeg',
    ]
    return render(request, 'galeria/galeria.html', {'imagenes': imagenes})
