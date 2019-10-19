#v2 creating a dictionary out of the csv to count items

import csv

file = 'C:\\Users\\dminahan\\python\\velocity\\Consumer_velocity.csv'
with open(file) as fh:
    rd = csv.DictReader(fh, delimiter=',')
    for row in rd:
        print(row)   
    
