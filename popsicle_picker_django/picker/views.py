from django.shortcuts import render
from picker.models import Pop


def picker(request):
    return render(request, 'picker/main.html')

def result(request):
    pop = Pop.objects.order_by("?").first()
    context = {'name': pop.name, 'image': pop.image}
    return render(request, 'picker/result.html', context)