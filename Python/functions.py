import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def pageURL(URL):
    page = requests.get(URL, headers=headers)
    return (page)

def itemInput(URLinput):
    item = input("Enter what product you would like to search for:")
    item = item.replace(" ", "+")
    URLinput = URLinput + item
    return URLinput

def URLinput(page):
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')
    return(soup2)

def printInfo(soup):
    results = soup.find_all('a', attrs={"class":"a-link-normal a-text-normal"})
    return(results) 