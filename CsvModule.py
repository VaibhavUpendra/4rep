import csv
with open('Stock_Data.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)