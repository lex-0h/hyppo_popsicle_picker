from picker.picker import get_pop_pack
from django.shortcuts import render
from django.template import loader

# Create your views here.
def picker(request):
    return render(request, 'picker/main.html')

def result(request):
    pop = get_pop_pack()
    return render(request, 'picker/result.html', pop)