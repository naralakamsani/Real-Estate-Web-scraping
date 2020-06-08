import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("https://www.century21.com/real-estate/dallas-tx/LCTXDALLAS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content

soup = BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"infinite-container"})

l=[]

for items in all:
    
    address = items.find_all("div",{"class":"property-address"})
    cities = items.find_all("div",{"class":"property-city"})
    beds = items.find_all("div",{"class":"property-beds"})
    baths = items.find_all("div",{"class":"property-baths"})
    areas = items.find_all("div",{"class":"property-sqft"})
    prices = items.find_all("a",{"class":"listing-price"})
    
    for address, city,bed,bath,sqft,price in zip(address,cities,beds,baths,areas,prices):
        
        d={}
        
        try:
            d["Address"]=address.text.replace("\n","").replace("   ","")
        except:
            pass
        
        try:
            d["City"]=city.text.replace("\n","").replace("  ","")
        except:
            pass
        
        try:
            d["Bed's"]=bed.find("strong").text
        except:
            pass
        
        try:
            d["Bath's"]=bath.find("strong").text
        except:
            pass
        
        try:
            d["SqFt"]=sqft.find("strong").text
        except:
            pass
        
        try:
            d["Price"]=price.text.replace("\n","").replace(" ","")
        except:
            pass
        l.append(d)

df=pandas.DataFrame(l)

df.to_csv("Current_Realestate.csv")
