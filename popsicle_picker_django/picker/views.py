from picker.picker import get_pop_pack
from django.shortcuts import render
from django.template import loader


def picker(request):
    return render(request, 'picker/main.html')

def result(request):
    # pop = get_pop_pack()
    # for testing:
    pop = {'image': '/static/picker/test_image.jpg', 'name': 'Toasted Buckeye: 3-tiered', 'image_alt': ''}
    return render(request, 'picker/result.html', pop)