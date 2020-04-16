from WalmartScrape import WalmartScrape
from BestBuyScrape import BestBuyScrape
from BH import BHscrape

#filling list with products
data = []
def listInput(lines, data):
    for line in lines: 
        line = line.strip()
        products_strings = line.split('@')
        products = [str(n) for n in products_strings]
        data.append(products)
    for i in range(0, len(data)):
        data[i][1] = float(data[i][1])
        data[i][2] = float(data[i][2])


def prodPrice(val):
    return val[1]

def prodRating(val):
    return val[2]

def fileOpening(website):
    file = open (website, 'r')
    lines = file.readlines()
    file.close()
    listInput(lines, data)


def runSort(sort):
    fileOpening('BBproducts')
    fileOpening('WMproducts')
    #fileOpening('BHproducts')
    
    if sort == 1:
        data.sort(key= prodPrice)
    if sort == 2:
        data.sort(key= prodRating, reverse=True)

def printList():
    for j in range(0, len(data)):
        print('------------------------------------')
        print(data[j][0])
        print(data[j][1])
        print(data[j][2])
        
item = 'cpu'

WalmartScrape(item)
BestBuyScrape(item)
runSort(1)
printList()

