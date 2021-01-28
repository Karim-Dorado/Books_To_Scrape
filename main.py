from books import *
from category import *
from categories_list import *

for cat in scrape_cat_list():
    for url in scrape_cat(cat):
        print(scrape_book(url)['category'])
