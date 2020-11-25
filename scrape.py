import requests
from bs4 import BeautifulSoup


def scrape_func():
    URL = 'https://www.newegg.com/p/pl?d=3080&PageSize=96&N=100006662&LeftPriceRange=600+1000'
    # URL = 'https://www.newegg.com/Processors/EventSaleStore/ID-10493'
    page = requests.get(URL)

    html_soup = BeautifulSoup(page.text, 'html.parser')

    movie_containers = html_soup.find_all(
        'div', class_='item-cells-wrap')

    all_links = []
    for div in movie_containers:
        buttons = div.find_all('button', class_='btn btn-primary btn-mini')
        for index, button in enumerate(buttons):
            if button.text == 'Add to cart ':
                linkdiv = buttons[index].parent.parent.parent.parent
                link = linkdiv.find_all('a')
                all_links.append(str(link[0]['href']))

    return all_links
