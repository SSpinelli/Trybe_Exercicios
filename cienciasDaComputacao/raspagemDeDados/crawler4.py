from parsel import Selector
import requests


URL_BASE = "https://finance.yahoo.com/trending-tickers"

request = requests.get(URL_BASE)

selector = Selector(text=request.text).css("tr")


def tratarInfo(array):
    for info in array:
        symbol_info = info.css("a::text").get()
        name_info = info.css("td::text").get()
        last_price = info.css("fin-streamer::text").get()

        if symbol_info is not None:
            print(f"{symbol_info}: {name_info} last price: {last_price}")


for row in selector:
    info_stock = row.css("tr")
    tratarInfo(info_stock)
