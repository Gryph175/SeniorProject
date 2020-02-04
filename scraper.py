import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Bose-Cancelling-Wireless-Bluetooth-Headphones/dp/B07Q9MJKBV/ref=sr_1_7?crid=38E00HSWV2N1X&keywords=bose+headphones&qid=1580314150&sprefix=bose+head%2Caps%2C160&sr=8-7'
URL2 = 'https://www.amazon.com/Fire-TV-Stick-with-Alexa-Voice-Remote/dp/B0791TX5P5/ref=zg_bs_electronics_home_1?_encoding=UTF8&psc=1&refRID=Q2R39K2JCW8FV93TMJP6'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page1 = requests.get(URL, headers=headers)
page2 = requests.get(URL2, headers=headers)

def URLinput(page):
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    return(soup2)




soup = URLinput(page1)
soup2 = URLinput(page2)





def printInfo(item):
    title = item.find(id="productTitle").get_text()
    price = item.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])
    rating = item.find(id = "acrPopover").get_text()
    print(title.strip())
    print(price.strip())
    print(converted_price)
    print(rating.strip())






printInfo(soup)
printInfo(soup2)





