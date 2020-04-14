import requests
from bs4 import BeautifulSoup
from functions import scrapePrep, pageURL

def BestBuyScrape(product):
    BestBuyURL = "https://www.bestbuy.com/site/searchpage.jsp?st="
    BestBuyID = "image-link"

    file = open('BBurls', 'w')

    results = scrapePrep(BestBuyURL, BestBuyID, product)
    file.write(str(results))
    file.close
    file = open('BBurls', 'r')
    lines = file.readlines()
    file.close()
    file = open("BBurls", "w")

    #looking for specific product URLS to find info needed 

    for line in lines: 
        line = line.strip()
        if line.find('</a>, <a class="image-link" href=') != -1:
            line = line.replace('</a>, <a class="image-link" href="', 'https://www.bestbuy.com')
            line = line.replace('">', '')
            file.write(line + "\n")
    file.close()

    file = open('BBurls', 'r')
    lines = file.readlines()
    file.close()

    file = open('BBproducts', 'w')

    for line in lines: 
        line = line.strip()
        productSoup = pageURL(line)

        title = productSoup.find(class_="heading-5 v-fw-regular").get_text()
        price = productSoup.find('div', attrs={'class': 'priceView-hero-price priceView-customer-price'}).get_text()
        price = price.replace(' ', '')
        price = price.replace('Yourpriceforthisitemis$', '')
        price = price.replace('\n','')
        priceln = int((len(price))/2) + 1
        price = price[1:priceln]
        price = price.replace(',', '')
        rating = productSoup.find('p', class_="sr-only").get_text()
        rating = rating.replace('Rating, ', '')
        rating = rating.replace('out', ' ')
        rating = rating.strip()
        rating = rating[0:3]
        if rating.find('Be the first') != -1:
            rating = "0"

        file.write(title.strip() + '@')
        file.write(price.strip() + '@')
        file.write(rating.strip() + '\n')
   

    


BestBuyScrape('cpu')        



