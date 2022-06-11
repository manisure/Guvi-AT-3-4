from bs4 import BeautifulSoup
import requests

class Suman:
    url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'lxml')

    def Data_Content(self):
        return self.soup

    def Flipkart(self):
        return self.soup.prettify()

    def Name(self):
        name = self.soup.find('div', class_='_4rR01T')
        return name.text

    def Price(self):
        price = self.soup.find('div', class_='_30jeq3 _1_WHN1')
        return price.text

    def All_Data(self):
        products = []
        price = []

        for data in self.soup.findAll('div', class_='_3pLy-c row'):
            product_name = data.find('div', class_='_4rR01T')
            product_price = data.find('div', class_='_30jeq3 _1_WHN1')
            products.append(product_name.text)
            price.append(product_price.text)
        print(products)
        print("-------------------------------------------------------------------")
        print(price)



s = Suman()

s.All_Data()
