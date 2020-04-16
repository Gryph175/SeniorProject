from sort import runSort, printList
from WalmartScrape import WalmartScrape
from BestBuyScrape import BestBuyScrape
from BH import BHscrape

def websites(item):
    WalmartScrape(item)
    BestBuyScrape(item)
    #BHscrape(item)
    runSort(1)
    printList()
    
websites('gaming mouse')

#item = input("Enter what product you would like to search for:")
#websites(item)


