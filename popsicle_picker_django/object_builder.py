from picker.models import Pop
from picker.picker import pop_packs

for pop_pack in pop_packs:
    if Pop.objects.filter(name=pop_pack['name']).exists():
        pass
    else:
        # set image_alt to empty string; later, filter by image_alt='' and then put those into a list for processing
        new_object = Pop(name=pop_pack['name'], image=pop_pack['image'], image_alt='')
        new_object.save()

needs_alt = Pop.objects.filter(image_alt='')