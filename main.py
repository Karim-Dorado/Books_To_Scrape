import os
import csv
import requests
import books
import category
import categories_list


def main():
    """
    This function makes a request from the web site http://books.toscrape.com/,
    and returns a dict of each book from each category belonging to this web site.
    It doesn't need any parameter.
    """
    books_details = {}
    categories = categories_list.scrape_cat_list()
    directory = "Books_to_Scrape"
    try:
        os.mkdir(os.path.join(os.getcwd(), directory))
        os.chdir(os.path.join(os.getcwd(), directory))
    except FileExistsError:
        print(f"Error : File {directory} already exists !"
              "\nPlease rename/delete it if you want this utility runs correctly.")
        exit()
    for i in range(len(categories)):
        cat = category.scrape_cat(categories[i])
        name = categories[i].split('/')[6].translate({ord(c): None for c in '_0123456789'}).capitalize()
        print("Collecting data from :", name)
        books_details[name] = []
        try:
            os.mkdir(os.path.join(os.getcwd(), name))
            os.chdir(os.path.join(os.getcwd(), name))
        except FileExistsError:
            print(f"Error : File {name} already exists ! "
                  "\nPlease rename/delete it if you want this utility runs correctly.")
            exit()
        for url in cat:
            book = books.scrape_book(url)
            books_details[name].append(book)
            filename = f'{name}.csv'
            with open(filename, "w", newline='', encoding='utf-8') as f:
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
                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
                writer.writeheader()
                for value in books_details[name]:
                    writer.writerow(value)
        img_dir = "Images"
        try:
            os.mkdir(os.path.join(os.getcwd(), img_dir))
            os.chdir(os.path.join(os.getcwd(), img_dir))
        except FileExistsError:
            print(f"Error : File {img_dir} already exists ! "
                  "\nPlease rename/delete it if you want this utility runs correctly.")
            exit()
        for image_url in books_details[name]:
            r = requests.get(image_url['image_url'])
            image_name = f'{image_url["title"]}.jpg'.translate({ord(':'): None,
                                                                ord('/'): None,
                                                                ord('*'): None,
                                                                ord('"'): None,
                                                                ord('?'): None,
                                                                ord('<'): None,
                                                                ord('>'): None,
                                                                ord('|'): None})
            if r.ok:
                with open(image_name, 'wb') as f:
                    f.write(r.content)
        print("Data collected from :", name)
        books_details = {}
        os.chdir("../..")


if __name__ == '__main__':
    main()
