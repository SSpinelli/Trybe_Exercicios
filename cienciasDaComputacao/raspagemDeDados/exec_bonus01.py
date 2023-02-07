# Agora um desafio! Vá ao site wikipedia
# e recupere as imagens de todas as bandeiras.

import requests
from parsel import Selector

base_url = "https://en.wikipedia.org"

url = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"

response = requests.get(url).text

selector = Selector(text=response)

flags_by_leter = selector.css("ul .gallerybox div a::attr(href)").getall()

for rest_of_url in flags_by_leter:
    print(f"{base_url}{rest_of_url}", sep="\n")
