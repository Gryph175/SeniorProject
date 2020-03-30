import requests
from bs4 import BeautifulSoup
from functions import pageURL, itemInput, URLinput, pageInfo

BHurl = 'https://www.bhphotovideo.com/c/search?Ntt='
BHID = 'more_3AHFX0SPjGtK8ii-kIXIau'


file = open('BHurls', 'w')

BHurl = itemInput(BHurl)
BHpage = pageURL(BHurl)
BHsoup = URLinput(BHpage)

print(BHurl)
results = pageInfo(BHsoup, BHID)
file.write(str(results))
file.close()
file = open('BHurls', 'r')
lines = file.readlines()
file.close()
file = open('BHurls', 'w')

for line in lines:
    line = line.strip()
    if line.find('<a class="more_3AHFX0SPjGtK8ii-kIXIau"') != -1:
        line = line.replace('</a>, <a class="more_3AHFX0SPjGtK8ii-kIXIau" data-selenium="miniProductPageSellingPointsDetailsLink" href="', 'https://www.bhphotovideo.com')
        line = line.replace('[<a class="more_3AHFX0SPjGtK8ii-kIXIau" data-selenium="miniProductPageSellingPointsDetailsLink" href="', 'https://www.bhphotovideo.com')
        line = line.replace('">', '')
        file.write(line + '\n')
file.close()

file = open('BHurls', 'r')
lines = file.readlines()
file.close()

for line in lines:
    line = line.strip()
    productPage = pageURL(line)
    productSoup = URLinput(productPage)

    title = productSoup.find(class_="title_3bJZzlB3PKkE_8ajs9mroe").get_text()
    price = productSoup.find(class_="price_1DPoToKrLP8uWvruGqgtaY").get_text()
    rating = productSoup.find(class_="starContainer_K6YXTdn52hu9mzQ1MV43G")

    print(title.strip())
    print(price.strip())
    print(rating)




