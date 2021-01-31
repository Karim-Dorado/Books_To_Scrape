import csv
from books import *
from category import *
from categories_list import *


def main():
    dico = {}
    categories = scrape_cat_list()
    for i in range(len(categories)):
        name = scrape_book(scrape_cat(categories[i])[0])['category']
        category = scrape_cat(scrape_cat_list()[i])
        print("Collecting data from :", name)
        dico[name] = []
        for url in category:
            book = scrape_book(url)
            dico[name].append(book)
            filename = "%s.csv" % name
            with open(filename, "w", newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'title',
                    'upc',
                    'price_excluding_tax',
                    'price_including_tax',
                    'number_available',
                    'product_description',
                    'review_rating',
                    'category',
                    'image_url'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for ind in dico[name]:
                    writer.writerow({
                        'title': ind['title'],
                        'upc': ind["upc"],
                        'price_excluding_tax': ind['price_excluding_tax'],
                        'price_including_tax': ind['price_including_tax'],
                        'number_available': ind['number_available'],
                        'product_description': ind['product_description'],
                        'review_rating': ind['review_rating'],
                        'category': ind['category'],
                        'image_url': ind['image_url']
                    })

        print("Data collected from :", name)
        dico = {}


if __name__ == '__main__':
    main()
