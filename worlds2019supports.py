import csv
import requests
import urllib.request
from bs4 import BeautifulSoup

excelfile = open('worlds2019sup.csv', 'w' , newline ='')
writer = csv.writer(excelfile)

url = requests.get("https://bit.ly/2oCOqBc")
soup = BeautifulSoup(url.content, 'lxml')

tbody = soup('table', {"class":"wikitable sortable spstats plainlinks hoverable-rows"})[0].find_all('tr')


for row in tbody:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)
print(len(tbody))
excelfile.close()
