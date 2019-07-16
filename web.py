import requests
from bs4 import BeautifulSoup
import csv
pag= 15
while pag: 
    url='http://evaluare.edu.ro/Evaluare/CandFromJudIAD.aspx?Jud=4&Poz=0&PageN='
    url=url + str(pag)
    r=requests.get(url)
    html=r.content  
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)
    table = soup.find("table", attrs={"class":"mainTable"})
    #print(table)

    
    #data = table.get_text()
    #data1 = table.find_all("tr")[n]
    #print(data1)
    print ("+++++++++++++++++++++++++++++Lucru boss pagina: " + str(pag) + "!+++++++++++++++++++++++++++++")
    headings = ["Index","NUmele Candidatului","Pozitia in ieraria Evaluare Nationala 2019","Scoala de Provenienta","Limba si literatura romana -nota","Limba si literatura romana -Contestatie","Limba si literatura romana -nota finala","Matematica-nota","Matematica-contestatie","Matematica-finala","Limba-Materna Denumire","Limba-Materna nota","Limba Materna contestatie","Limba-Materna nota-finala","medie"]

    #print(headings)
    for row in table.find_all("tr")[2:]:
        dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
        f = open('dict.csv','a',encoding='UTF-8')
        w = csv.DictWriter(f,dataset.keys())
        w.writerow(dataset)
        f.close()
    pag = pag - 1
print ("+++++++++++++++++++++++++++++Gata Boss!+++++++++++++++++++++++++++++")   