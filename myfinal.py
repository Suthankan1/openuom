import requests
import json
import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price
    l_txt = requests.get(product_laughs).text
    l_soup = BeautifulSoup(l_txt,'html.parser')
    lprice = l_soup.find_all('span', class_="price")
    lpname = l_soup.find('h1').text
    
    
    for i in lprice:
        j = i.text.strip('Rs.')
        lprice=float(j)
    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    url = product_glomark

    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    data = [
        json.loads(x.string) for x in soup.find_all("script", type="application/ld+json")
    ]

# Extracting the price value
    price = None
    for item in data:
        m=item['name']
        offers = item.get("offers", {})  # Get offers dict or empty dict if not found
    for i in offers:
        k=i['price']
        
    gname=m
    gprice=float(k)


    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    product_name_laughs = lpname
    product_name_glomark = gname
    price_laughs = lprice
    price_glomark = gprice
    #TODO: Parse the values as floats, and print them.
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')