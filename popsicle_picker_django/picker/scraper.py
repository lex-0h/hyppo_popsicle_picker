from bs4 import BeautifulSoup
from urllib.request import urlopen
from picker.models import Pop

page = urlopen('https://www.thehyppo.com/pop-delivery?category=All+Flavors')
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

product_list = soup.find_all('h1', class_= 'ProductList-title')
pop_list = []
 
for product in product_list:
    pop_name = product.get_text()
    if pop_name != 'Random Pop':
        pop_list.append(pop_name)

# find all img tags that have a data-src attribute (because attribute is mostly productList specific)
image_elements = soup.find_all('img', {'data-src': True})
# get a list of data-src attribute values alone and remove the first one because that is the header img
images = [element['data-src'] for element in image_elements][1::2]
# last image is for the random pop, so remove it
images.pop()
# pack the images and pop_list lists together to be grabbed by the view. the indices should line up
pop_packs = [{'image': images[i], 'name': pop_list[i]} for i in range(len(pop_list) - 1)]

Pop.objects.bulk_create([Pop(**pop) for pop in pop_packs])