# write csv

import csv 
from datetime import datetime


def write_to_csv(data):
    date = datetime.now().strftime('%Y-%m-%d')
    with open('data-temperature-{}.csv' .format(date), 'a', newline = '', encoding = 'utf-8') as file: 
        filewriter = csv.writer(file)
        filewriter.writerow(data)
    

write_to_csv(['กทม',20.5])
