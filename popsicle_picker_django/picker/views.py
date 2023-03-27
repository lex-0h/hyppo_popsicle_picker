from django.shortcuts import render
from picker.models import Pop


def picker(request):
    return render(request, 'picker/main.html')

def result(request):
    pop = dict(Pop.objects.order_by("?").first())
    # for testing:
    # pop = {'image': '/static/picker/test_image.jpg', 'name': 'Toasted Buckeye: 3-tiered', 'image_alt': ''}
    return render(request, 'picker/result.html', pop)