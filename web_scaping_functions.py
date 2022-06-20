import requests
from bs4 import BeautifulSoup
import pandas as pd




HEADERS = ({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36', 
'Accept-Language': 'en-US,en;q=0.8;q=0.5',})







def trendyolWebScapingFunction(productName:str):

    search_query = productName.replace(' ', '+')
    base_url = 'https://www.trendyol.com/sr?q={0}'.format(search_query)

     
    items = []
    for i in range(1, 3):
        # print('Processing {0}...'.format(base_url + '&pi={0}'.format(i)))
        response = requests.get(base_url + '&pi={0}'.format(i),headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')

        results = soup.find_all('div', {'class': 'p-card-wrppr'})
    
        for result in results:
            product_name = result.find('span',{'class':'prdct-desc-cntnr-name'}).text

            try:
                price = result.find('div', {'class': 'prc-box-dscntd'}).text.replace(".","",1).replace(",",".").replace(" TL","")
                # print(product_name, price)
                items.append([product_name, price])
            except AttributeError:
                continue
        
        
    df = pd.DataFrame(items, columns=['product', 'price']) 
    df.sort_values('price', ascending=False)
    df['price'] = df['price'].astype('float')
    df = df.nlargest(2,'price')
    productTitle = df['price'].iloc[0]
    productPrice = df['product'].iloc[0]

    return {"title":productTitle,"price":productPrice}



def amazonWebScapingFunction(productName:str):

    search_query = productName.replace(' ', '+')
    base_url = 'https://www.amazon.com.tr/s?k={0}'.format(search_query)

    items = []
    for i in range(1, 3):
        # print('Processing {0}...'.format(base_url + '&page={0}'.format(i)))
        response = requests.get(base_url + '&page={0}'.format(i), headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})

        for result in results:
            product_name = result.h2.text

            try:
                price1 = result.find('span', {'class': 'a-price-whole'}).text.replace(",","").replace(".","")
                price2 = result.find('span', {'class': 'a-price-fraction'}).text.replace(",","")
                price2 = "." + price2
                price = float(price1 + price2)
                
                items.append([product_name,price])
            except AttributeError:
                continue
 
    
    df = pd.DataFrame(items, columns=['product','price'])
    
    
    df = pd.DataFrame(items, columns=['product', 'price']) 
    df.sort_values('price', ascending=False)
    df['price'] = df['price'].astype('float')
    df = df.nlargest(2,'price')
    productTitle = df['product'].iloc[0]
    productPrice = df['price'].iloc[0]

    return {"title":productTitle,"price":productPrice}





def hepsiburadaWebScapingFunction(productName:str):

    search_query = productName.replace(' ', '+')
    base_url = 'https://www.hepsiburada.com/ara?q={0}'.format(search_query)

     
    items = []
    for i in range(1, 3):
        print('Processing {0}...'.format(base_url + '&sayfa={0}'.format(i)))
        response = requests.get(base_url + '&sayfa={0}'.format(i),headers=HEADERS)
        soup = BeautifulSoup(response.content, 'html.parser')

        results = soup.find_all('li', {'class': 'productListContent-item'})
    
        for result in results:
            product_name = result.h3.text 

            try:
                price = result.find('div', {'data-test-id': 'price-current-price'}).text.replace(".","",1).replace(",",".").replace(" TL","")
                # print(rating_count, product_url)
                items.append([product_name, price])
            except AttributeError:
                continue
 

 
        
        
    df = pd.DataFrame(items, columns=['product', 'price']) 
    df.sort_values('price', ascending=False)
    df['price'] = df['price'].astype('float')
    df = df.nlargest(2,'price')
    productTitle = df['price'].iloc[0]
    productPrice = df['product'].iloc[0]

    return {"title":productTitle,"price":productPrice}