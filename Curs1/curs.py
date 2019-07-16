import requests
import csv

url='https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv'


class GetStockFinance():
    
    def __init__ (self,url):
        self.url=url
        #self.stockindex = stockindex
        
    def get_stoc_finance(self):
        download =requests.get(self.url) 
        
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)  

r=GetStockFinance(url)
r.get_stoc_finance()