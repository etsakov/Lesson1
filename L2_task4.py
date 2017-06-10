import csv

file_name = 'answers.csv'

answers = [
    ["привет","И тебе привет!"],
    ["как дела","Лучше всех"],
    ["пока","Увидимся"]
]

with open(file_name, 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(answers)

# Find our why am unable to extend the list each time when add an answer

key = input('Give a key ')
meaning = input('Give a meaning ')

with open(file_name, 'a', newline="") as file:
    answer = [key, meaning]
    writer = csv.writer(file)
    writer.writerow(answer)