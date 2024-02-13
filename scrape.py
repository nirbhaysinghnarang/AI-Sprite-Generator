"""
One-time script to generate schema of sprite configurations from [https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/]
"""
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import json



url = "https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
roots = soup.find_all('h3')


"""
<root>
    <ul>
        <li> 
            <ul>

"""


def is_base(ul):
    return ul.find('ul', recursive=True) is not None


def get_base_options(ul, k=0):
    lst = [label.text.strip() for label in ul.find_all('label', recursive=True)]
    return lst[:k]


def process_ul(ul):
    items = []
    nested_items = ul.find_all('li', recursive=False)
    for item in nested_items:
        item_title = item.find('span').text
        if is_base(item):
            items.append({item_title:get_base_options(item, k=10)})
            continue
        nested_items = []
        nested_uls = item.find_all('ul')
        for ul in nested_uls:
            nested_items.append(process_ul(nested_ul))
        items.append({item_title:nested_items})
    return items

schema = []
for root in roots:
    nested_ul = root.find_next('ul')   
    root_data = process_ul(nested_ul)
    if root_data:
        schema.append({root.text:root_data})



filename = 'schema.json'
with open(filename, 'w') as file:
    json.dump(schema, file, indent=4)