import csv
import json

with open('day-08\example1.csv','r') as file:
    reader =csv.reader(file)
    next(reader)

    for line in reader:
        print(line[0])


with open('day-08\example2.json','r') as file1:
    data = json.load(file1)
    print(data)
