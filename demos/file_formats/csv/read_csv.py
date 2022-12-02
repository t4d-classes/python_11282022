import csv
import itertools


with open('cities.csv', encoding="UTF-8") as csvfile:

    csvreader = csv.reader(csvfile)

    next(csvreader)

    for row in itertools.islice(csvreader, 0, 5):
        print(row)