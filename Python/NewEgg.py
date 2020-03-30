import requests
from bs4 import BeautifulSoup
from functions import pageURL, itemInput, URLinput, pageInfo

NewEggURL = "https://www.newegg.com/p/pl?d="
NewEggID = "item-title"

file = open('NEurls', 'w')

NewEggURL = itemInput(NewEggURL)
NewEggPage = pageURL(NewEggURL)
NewEggSoup = URLinput(NewEggPage)

print(NewEggURL)
results = pageInfo(NewEggSoup, NewEggID)
file.write(str(results))
file.close
file = open('NEurls', 'r')
lines = file.readlines()
file.close()
file = open('NEurls', 'w')

for line in lines: 
    line = line.strip()
    if line.find('<a class="item-title" href=') != -1:
        line = line.replace('</a>, <a class="item-title" href="', '')
        line = line.replace('[<a class="item-title" href="', '')
        line = line.replace('">', '')
        file.write(line + '\n')
file.close

file = open('NEurls', 'r')
print('test')
lines = file.readlines()
file.close()

for line in lines: 
    line = line.strip()
    productPage = pageURL(line)
    productSoup = URLinput(productPage)

    price = productSoup.find  ('div', attrs={'class':"price-current"})

    print(price)