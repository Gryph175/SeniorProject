from flask import Flask, jsonify, render_template, request, redirect, url_for
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
    
    if sort == 1:
        data.sort(key= prodPrice)
    if sort == 2: 
        data.sort(key= prodPrice, reverse=True)
    if sort == 3:
        data.sort(key= prodRating)
    if sort == 4:
        data.sort(key= prodRating, reverse=True)

def printList():
    file = open('Products', 'w')
    for j in range(0, len(data)):
        #print('------------------------------------')
        file.write('------------------------------------' + '\n')
        #print(data[j][0])
        file.write(str(data[j][0]) + '\n')
        #print(data[j][1])
        file.write(str(data[j][1]) + '\n')
        #print(data[j][2])
        file.write(str(data[j][2]) + '\n')
    file.close()

def dataget():
    return data

def clearList():
    data.clear()


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index(): 
    if request.method == "POST":
        prod = request.form["product"]
        clearList()
        BestBuyScrape(prod)
        WalmartScrape(prod)
        fileOpening('BBproducts')
        fileOpening('WMproducts')
        return redirect(url_for("OutPage"))  
    else:
        return render_template("index.html")
        
    #item = 'keyboard'
    #BestBuyScrape(item)
    #WalmartScrape(item)
    #runSort(1)
    #return jsonify(dataget())


@app.route("/OutPut", methods=["POST", "GET"])  
def OutPage():
    data = dataget()
    if request.method == "POST":
        sort = request.form["sort"]
        if sort == '1':
            runSort(1)
        if sort == '2':
            runSort(2)
        if sort == '3':
            runSort(3)
        if sort == '4':
            runSort(4)
        return redirect(url_for("OutPage"))

    return render_template('OutPut.html', title='Tool-Active', data=data)



if __name__ == "__main__":
    app.run(debug=True)