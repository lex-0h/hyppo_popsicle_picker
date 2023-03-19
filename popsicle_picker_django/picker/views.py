from picker.picker import get_pop_pack
from django.shortcuts import render
from django.template import loader

# Create your views here.
def picker(request):
    template = loader.get_template('/templates/picker/main.html')
    return render(request, template)

def result(request, result):
    return render()