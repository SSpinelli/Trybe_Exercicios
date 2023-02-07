# Baseando-se em uma página contendo detalhes sobre um livro, faça a extração
# dos campos título, preço, descrição e url contendo a imagem de capa do livro.
import requests
from parsel import Selector


url = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"

book_info = requests.get(url).text

selector = Selector(text=book_info)

title = selector.css(".product_main h1::text").get()
price = selector.css(".product_main .price_color").re_first(r"£\d+\.\d{2}")
description = selector.css("#product_description + p::text").get()
image_url = selector.css("#product_gallery img::attr(src)").get()

if description.endswith("...more"):
    description = description[: -len("...more")]

print(title, price, description, image_url, sep="\n")
