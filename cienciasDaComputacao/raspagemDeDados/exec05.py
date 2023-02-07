# Modifique o exercício anterior para retornar também quantos
# livros estão disponíveis, apresentando como último campo no retorno.

import requests
from parsel import Selector


url = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"

book_info = requests.get(url).text

selector = Selector(text=book_info)

title = selector.css(".product_main h1::text").get()
price = selector.css(".product_main .price_color").re_first(r"£\d+\.\d{2}")
description = selector.css("#product_description + p::text").get()
image_url = url + selector.css("#product_gallery img::attr(src)").get()
stock = selector.css("table tr:nth-of-type(6) td::text").get()[10]

if description.endswith("...more"):
    description = description[: -len("...more")]

print(title, price, description, image_url, stock, sep="\n")
