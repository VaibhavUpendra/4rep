import csv
with open('Stock_Data.csv','r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

with open("output.csv", 'w') as file:
    writer = csv.writer(file,delimiter=':')
    writer.writerow(['name','age','city'])
    writer.writerow(['Raheem',22,'Kannur'])
    writer.writerow(['John', 22, 'Kasargod'])



with open("dictoutput.csv", 'w') as file:
#   writer.writerow(['name','age','city'])
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Raheem','age': 22,'city': 'Kannur'})
    writer.writerow({'name': 'John','age': 22,'city': 'Kasargod'})

try:
    with open("Stock_Data.csv",'r') as file:
        reader = csv.reader(file)
        for orw in reader:
            print(row)
except csv.Error as e:
    print(f"Error reading CSV file: {e}")
except FileNotFoundError as e:
    print(f"No such file found")
except Exception:
    print("Something went wrong")


