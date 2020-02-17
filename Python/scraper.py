import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/s?k="
BestBuy = "https://www.bestbuy.ca/en-ca/search?search="
NewEgg = "https://www.newegg.com/p/pl?d="
Walmart = "https://www.walmart.com/search/?query=" 
Target = "https://www.target.com/s?searchTerm="

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

file = open("WebURLs", "w")

def pageURL(URL):
    page = requests.get(URL, headers=headers)
    return (page)

item = input("Enter what product you would like to search for:")
item = item.replace(" ", "+")
URL = URL + item

page1 = pageURL(URL)


def URLinput(page):
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    return(soup2)

soup = URLinput(page1)

def printInfo(item):
    results = soup.find_all('a', attrs={"class":"a-link-normal a-text-normal"})
    return(results)
   
print (URL)
results = printInfo(soup)
file.write(str(results))






