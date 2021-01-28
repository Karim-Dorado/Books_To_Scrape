import requests
from bs4 import BeautifulSoup


def scrape_cat_list():
    """
    This function makes a request from the web site book_toscrape.com,
    and returns a list of each category page belonging to this web site.
    :param : A string containing the URL of a category page
    ex:'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html'
    """
    url = 'http://books.toscrape.com'
    cat_url_list = []
#    cat_name_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ul = soup.find("ul", {"class": "nav nav-list"})
    a_list = ul.find_all('a')
    for a in a_list[1:]:
        cat_url_list.append('http://books.toscrape.com/' + a['href'])
#        cat_name_list.append(all_a[i].text.strip())
    return cat_url_list
