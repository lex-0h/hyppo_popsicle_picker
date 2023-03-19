import random
from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen('https://www.thehyppo.com/pop-delivery?category=All+Flavors')
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

product_list = soup.find_all('h1', class_= 'ProductList-title')
# The keys for this dict were generated using this program using <alt = {pop: '' for pop in pop_list}> in the
# command line. This is required because there is no alt usable alt text to scrape with the images. This 
# dict has to be manually updated when a new flavor is added to the webpage. I plan to add some code that 
# will automatically add a <pop: ''> entry into the dict so it'll only need to be filled with alt text, which
# will always have to be done manually (unless I could get an ai to do that...?)
alt = {
    'Toasted Buckeye: 3-tiered': 'A popsicle with a light brown base, chocolate brown middle, and cream-colored tip laying on a bed of peanuts and dark chocolate',
    'Chocolate Peppermint': 'A chocolate-brown popsicle on a bed of red and green candycane pieces dark chocolate surrounded by fresh mint',
    'Pumpkin Latte: Pop in a Pop': '',
    'Pink Grapefruit': '', 'Blueberry Cheesecake': '', 'Honeydew Green Tea': '',
    'Straight-Up Strawberry': '', 'Champagne Mango': '', 'Nutella': '', 
    'Avocado Coconut': '', 'Mexican Hot Chocolate': '', 'Blueberry Lavender Lemonade': '',
    'Mango Mojito': '', 'Pistachio Coconut': '', 'Elvis (Peanut Butter, Banana, Honey)': '',
    'Pineapple Orange': '', 'Strawberry Cheesecake': '', 'Key Lime': '',
    'Pineapple Cilantro': '', 'Horchata': '', 'Blackberry Goat Cheese': '',
    'Mango Habanero': '', 'Dark Roast Espresso': '', 'Coconut Coconut': '',
    'Watermelon': '', 'Orange Cream': '', 'Chocolate Sea Salt': '',
    'Strawberry Lemonade': '', 'Peanut Butter Pie': '', 'Pistachio Rosewater': ''
}
pop_list = []

for product in product_list:
    pop_name = product.get_text()
    if pop_name != 'Random Pop':
        pop_list.append(pop_name)




# find all img tags that have a data-src attribute (because attribute is mostly productList specific)
image_elements = soup.find_all('img', {'data-src': True})
# get a list of data-src attribute values alone and remove the first one because that is the header img
images = [element['data-src'] for element in image_elements][1:]
# pack the images and pop_list lists together to be grabbed by the view. the indices should line up
pop_packs = list(zip(images, pop_list))



def get_pop_pack():
    choice = random.randint(0, len(pop_packs) - 1)
    return pop_packs[choice]

print(get_pop_pack())
# pop_names = 
# print(product_list)