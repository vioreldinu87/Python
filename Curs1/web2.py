from bs4 import BeautifulSoup
import requests

import csv

url = 'http://bacalaureat.edu.ro/Pages/TaraRezultAlfa.aspx'

with requests.Session() as session:
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'}
    
    r=requests.post()
    
    
    
    
#     r=requests.get(url)
#     html=r.content  
#     soup = BeautifulSoup(html, 'html.parser')
#     #print(soup)
#     table = soup.find("table", attrs={"class":"mainTable"})
#     #print(table.encode('utf-8'))
# 
# headings = ["Index","NUmele Candidatului","Poz1","Scoala de Provenienta","Limba si literatura romana","nota","Limba si literatura romana","Contestatie","Limba si literatura","romana","nota finala","Matematica","nota","Matematica","contetatie","Matematica","finala","Limba","Materna","Denumire","Limba","Materna","nota","Limba Materna","contestatie","Limba","Materna","nota","finala","medie"]
# 
# for row in table.find_all("tr")[2:]:
#     dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
#     f = open('bac.csv','a',encoding='UTF-8')
#     w = csv.DictWriter(f,dataset.keys())
#     w.writerow(dataset)
#     f.close()
# print ("+++++++++++++++++++++++++++++Gata Boss!+++++++++++++++++++++++++++++")   
