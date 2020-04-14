import requests
from bs4 import BeautifulSoup
from functions import scrapePrep, pageURL

def BHscrape(product):
    BHurl = 'https://www.bhphotovideo.com/c/search?Ntt='
    BHID = 'more_3AHFX0SPjGtK8ii-kIXIau'

    file = open('BHurls', 'w')

    results = scrapePrep(BHurl, BHID, product)
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

    file = open('BHproducts', 'w')

    for line in lines:
        line = line.strip()
        productSoup = pageURL(line)

        title = productSoup.find(class_="title_3bJZzlB3PKkE_8ajs9mroe").get_text()
        price = productSoup.find(class_="price_1DPoToKrLP8uWvruGqgtaY").get_text()
        price = price.replace('$','')
        price = price.replace(',', '')
        #rating = productSoup.find(class_="starContainer_K6YXTdn52hu9mzQ1MV43G")

        print(title.strip())
        #print(price.strip())
        #print(rating)

        file.write(title.strip() + '@')
        file.write(price.strip() + '\n')




