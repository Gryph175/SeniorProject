import requests
from bs4 import BeautifulSoup
from functions import scrapePrep, pageURL

def WalmartScrape(product):
    WalmartURL = "https://www.walmart.com/search/?query="
    WalmartID = "product-title-link line-clamp line-clamp-2"

    file = open ('WMurls', 'w')

    results = scrapePrep(WalmartURL, WalmartID, product)
    file.write(str(results))
    file.close 
    file = open('WMurls', 'r')
    lines = file.readlines()
    file.close()
    file = open('WMurls', 'w')

    for line in lines: 
        line = line.strip()
        if line.find('<a class="product-title-link line-clamp line-clamp-2" data-type="itemTitles" href="') != -1:
            line = line.replace('</a>, <a class="product-title-link line-clamp line-clamp-2" data-type="itemTitles" href="', 'https://www.walmart.com/')
            line = line.replace('[<a class="product-title-link line-clamp line-clamp-2" data-type="itemTitles" href="', 'https://www.walmart.com/')
            line = line.replace('" lang="en" tabindex="-1">', '')
            file.write(line + "\n")
    file.close

    file = open('WMurls', 'r')
    lines = file.readlines()
    file.close()

    file = open ('WMproducts', 'w')

    for line in lines:
        line = line.strip()
        productSoup = pageURL(line)

        title = productSoup.find(class_="prod-ProductTitle font-normal").get_text()
        price = productSoup.find(class_="price-characteristic").get_text() + '.' + productSoup.find(class_="price-mantissa").get_text()
        price = price.replace('\n', '')
        price = price.replace(' ', '')
        price = price.replace(',', '')
        rating = productSoup.find(class_="seo-avg-rating").get_text()

        #print(title.strip())
        #print(price.strip())
        #print(rating.strip() + " out of 5 stars")

        file.write(title.strip() + '@')
        file.write(price.strip() + '@')
        file.write(rating.strip()+ '\n')

    file.close()


product = 'gaming mouse'

WalmartScrape(product)