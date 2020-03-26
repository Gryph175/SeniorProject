import requests
from bs4 import BeautifulSoup
from functions import pageURL, itemInput, URLinput, pageInfo

amazonURL = "https://www.amazon.com/s?k="
amazonID = "a-link-normal a-text-normal"

file = open("WebURLs", "w")

amazonURL = itemInput(amazonURL)
amazonPage = pageURL(amazonURL)
amazonSoup = URLinput(amazonPage)

print (amazonURL)
results = pageInfo(amazonSoup, amazonID) 
file.write(str(results))
file.close()
file = open("WebURLs", "r")
lines = file.readlines()
file.close()
file = open("WebURLs", "w")

#looking for correct product URLs 

for line in lines:
    line = line.strip()
    if line.find( "href=")!= -1:
        if line.find("/gp/slredirect/picassoRedirect.html") == -1:
            if line.find("http") == -1:
                line = line.replace('[<a class="a-link-normal a-text-normal" href="', 'https://www.amazon.com')
                line = line.replace('</a>, <a class="a-link-normal a-text-normal" href="', 'https://www.amazon.com')
                line = line.replace('">', '')
                file.write(line + "\n")
file.close()

file = open("WebURLs", "r")
lines = file.readlines()



for line in lines: 
    line = line.strip()
    productPage = pageURL(line)
    productSoup = URLinput(productPage)

    title = productSoup.find(id ="productTitle").get_text()
    price = productSoup.find(id="priceblock_ourprice").get_text()
    rating = productSoup.find(id="acrPopover").get_text()

    print(title.strip())
    print(price)
    print(rating.strip())

    




 








