# web scrapping temperature 
from urllib.request import urlopen 
from bs4 import BeautifulSoup
# write csv
import csv 
from datetime import datetime
#plot 
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 


def write_to_csv(data):
    date = datetime.now().strftime('%Y-%m-%d')
    with open('data-temperature-{}.csv' .format(date), 'a', newline = '', encoding = 'utf-8') as file: 
        filewriter = csv.writer(file)
        filewriter.writerow(data)

alldata = {}
def checktemp(ID):
    url  = 'https://www.tmd.go.th/province.php?id=' + str(ID)
    webopen =  urlopen(url)  #open website without chrome 
    html_page = webopen.read()  #read data from website
    webopen.close()  #close web

    data = BeautifulSoup(html_page, 'html.parser')  #convert code by bs4 for translate
    try:
        temp = data.find('td',{'class':'strokeme'})
        title= data.find('td',{'class':'title'})
        provinces = title.text.strip()
        temp = temp.text
        #print(city, temp)
        alldata[provinces] = temp 
    except:
        pass

for i in range(1,83):
    
    checktemp(i)
#print(alldata)


for k,v in alldata.items():
    data = [k,v]
    write_to_csv(data)


df = pd.read_csv('data-temperature-2022-05-08.csv')
        




   
