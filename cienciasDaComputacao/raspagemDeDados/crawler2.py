from parsel import Selector
import requests


response = requests.get("http://books.toscrape.com/")
selector = Selector(text=response.text)

thumb_url = selector.css(".image_container a::attr(href)").get()

thumb_request = requests.get(f"http://books.toscrape.com/{thumb_url}")

thumb_selector = Selector(text=thumb_request.text)

book_title = thumb_selector.css(".product_main h1").get()

print(book_title)

# first_book = requests.get(thumb_url)

# a = Selector(text=first_book.text)

# print(thumb_url)
