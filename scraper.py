import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Bose-Cancelling-Wireless-Bluetooth-Headphones/dp/B07Q9MJKBV/ref=sr_1_7?crid=38E00HSWV2N1X&keywords=bose+headphones&qid=1580314150&sprefix=bose+head%2Caps%2C160&sr=8-7'
URL2 = 'https://www.amazon.com/Apple-MacBook-1-8GHz-dual-core-Intel/dp/B07211W6X2/ref=sr_1_3?crid=1L2Q3JP00IKP0&keywords=macbook+pro&qid=1580317455&sprefix=mac%2Caps%2C168&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page1 = requests.get(URL, headers=headers)
page2 = requests.get(URL2, headers=headers)

soup1 = BeautifulSoup(page1.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
soup3 = BeautifulSoup(page2.content, 'html.parser')
soup4 = BeautifulSoup(soup3.prettify(), 'html.parser')

title = soup2.find(id="productTitle").get_text()
price = soup2.find(id="priceblock_ourprice").get_text()
converted_price = float(price[1:6])
rating = soup2.find(id = "acrPopover").get_text()

title2 = soup4.find(id="productTitle").get_text()
price2 = soup4.find(id="priceblock_ourprice").get_text()
converted_price2 = float(price2[1:4])
rating2 = soup4.find(id = "acrPopover").get_text()

print(title.strip())
print(price.strip())
print(converted_price)
print(rating.strip())

print(title2.strip())
print(price2.strip())
print(converted_price2)
print(rating2.strip())
