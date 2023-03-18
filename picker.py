import random
from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen('https://www.thehyppo.com/pop-delivery?category=All+Flavors')
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

product_list = soup.find_all('h1', class_= 'ProductList-title')
pop_list = []

for product in product_list:
    pop_name = product.get_text()
    if pop_name != 'Random Pop':
        pop_list.append(pop_name)


def get_pop():
    choice = random.randint(0, len(pop_list) - 1)
    return pop_list[choice]

print(get_pop())



# pop_names = 
# print(product_list)