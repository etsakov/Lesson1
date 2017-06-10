import csv
 
file_name = "answers.csv"

with open(file_name, 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], ' - ', row[1])