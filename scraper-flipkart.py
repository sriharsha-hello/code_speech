from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl = 'https://www.flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off'

uclient = uReq(myurl)
page_html = uclient.read()
uclient.close()
page_soup =soup(page_html,"html.parser")

containers = page_soup.find_all("div",{"class":"col _2-gKeQ"})
#print(len(containers)) # prints the length or number of items in flipkart web page
#print(soup.prettify(containers[0])) #gives html code of 1 st item in flikart web page
container=containers[0]
#print(container.div.img["alt"]) # gives item title or item name
price = container.find_all("div",{"class":"col col-5-12 _2o7WAb"})
#print(price[0].text) # gives item cost or prce of the product
ratings =container.find_all("div",{"class":"niH0FQ"})
#print(ratings[0].text)

filename="products.csv"
f=open(filename,"w")

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name=container.div.img["alt"]

    price_container=container.find_all("div",{"class" : "col col-5-12 _2o7WAb"})
    price=price_container[0].text.strip()
    #print("price:"+price)


    #rating_container = container.find_all("div", { "class" : "niH0FQ"})
    #rating = rating_container[0].text

    #print("product name:"+product_name)
    #print("price:"+price)
    #print("rating:"+rating)

    #string parsing

    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price="Rs." + rm_rupee[1]
    split_price=add_rs_price.split('E')
    final_price = split_price[0]

    print(product_name.replace(".","|")+","+final_price+"\n")
    f.write(product_name.replace(".","|")+","+final_price+"\n")
f.close()

