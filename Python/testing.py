from sort import runSort
from WalmartScrape import WalmartScrape
from BestBuyScrape import BestBuyScrape
from BH import BHscrape

def websites(item):
    WalmartScrape(item)
    BestBuyScrape(item)
    BHscrape(item)
    runSort()

item = input("Enter what product you would like to search for:")
websites(item)


