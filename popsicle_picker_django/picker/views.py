from picker.picker import get_pop_pack
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse(get_pop_pack())