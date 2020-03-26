import requests
from bs4 import BeautifulSoup
from functions import pageURL, itemInput, URLinput, pageInfo

BestBuyURL = "https://www.bestbuy.com/site/searchpage.jsp?st="
BestBuyID = "image-link"

file = open('BBurls', 'w')

BestBuyURL = itemInput(BestBuyURL)
BestBuyPage = pageURL(BestBuyURL)
BestBuySoup = URLinput(BestBuyPage)


print(BestBuyURL)
results = pageInfo(BestBuySoup, BestBuyID)
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
    productPage = pageURL(line)
    productSoup = URLinput(productPage)

    title = productSoup.find(class_="heading-5 v-fw-regular").get_text()
    price = productSoup.find('div', attrs={'class': 'priceView-hero-price priceView-customer-price'}).get_text()
    price = price.replace(' ', '')
    price = price.replace('Yourpriceforthisitemis$', '')
    price = price.replace('\n','')
    priceln = int((len(price))/2) + 1
    price = price[0:priceln]
    file.write(price)
    rating = productSoup.find('p', class_="sr-only").get_text()
    if rating.find('Be the first') != -1:
        rating = "No reviews avaliable"

    print(title.strip())
    print(price.strip())
    print(rating.strip() + "\n")
   

    


        




