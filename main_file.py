from emailtome import email_func
from scrape import scrape_func


def main_scraper():
    items = scrape_func()

    if items:
        email_func(items)
