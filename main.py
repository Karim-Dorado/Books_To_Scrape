import requests
from bs4 import BeautifulSoup
from word2number import w2n


def scrape_book(url):
    """
    This function makes a request of a product page from the web site http://books.toscrape.com/,
    and returns a dictionary with the data we want to extract from this product page.
    :param : A string containing the URL of a product page
    ex:'http://books.toscrape.com/catalogue/sharp-objects_997/index.html'
    """
    r = requests.get(url)
    if r.ok:
        encoding = r.encoding if "charset" in r.headers.get("content-type", "").lower() else None
        soup = BeautifulSoup(r.content, from_encoding=encoding, features="html.parser")
        body = soup.find('body')
        title = body.h1.text
        tds = body.find_all('td')
        upc = tds[0].text
        price_excluding_tax = tds[2].text[1:]
        price_including_tax = tds[3].text[1:]
        number_available = tds[5].text.removeprefix('In stock (').removesuffix(' available)')
        ps = body.find_all('p')
        product_description = ps[3].text
        review_rating = w2n.word_to_num(" ".join(ps[2]['class'][:10]))
        a = soup.find_all('a')
        category = a[3].text
        image_url = 'http://books.toscrape.com' + body.img['src'][5:]
        return {
            'title': title,
            'upc': upc,
            'price_excluding_tax': price_excluding_tax,
            'price_including_tax': price_including_tax,
            'number_available': number_available,
            'product_description': product_description,
            'review_rating': review_rating,
            'category': category,
            'image_url': image_url
        }
    else:
        print("Error", r.status_code)


def scrape_cat(url):
    """
    This function makes a request from a category page of the web site http://books.toscrape.com/,
    and returns a list containing the URL of the Product page of each book belonging to this category
    :param : A string containing the URL of a category page
    ex:'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'
    """
    url_list = []
    r = requests.get(url)
    if r.ok:
        encoding = r.encoding if "charset" in r.headers.get("content-type", "").lower() else None
        soup = BeautifulSoup(r.content, from_encoding=encoding, features="html.parser")
        body = soup.find('body')
        li = body.find("li", {"class": "current"})
        try:
            nb_pages = int(li.text.split()[3])
            cat_list = [url[:-10] + 'page-' + str(i) + '.html' for i in range(2, nb_pages + 1)]
            cat_list.insert(0, url)
        except AttributeError:
            cat_list = [url]
        for url in cat_list:
            r = requests.get(url)
            if r.ok:
                encoding = r.encoding if "charset" in r.headers.get("content-type", "").lower() else None
                soup = BeautifulSoup(r.content, from_encoding=encoding, features="html.parser")
                h3s = soup.find_all('h3')
                for h3 in h3s:
                    url_list.append("http://books.toscrape.com/catalogue" + h3.a['href'][8:])
    return url_list


for url in scrape_cat("http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"):
    print(scrape_book(url))
