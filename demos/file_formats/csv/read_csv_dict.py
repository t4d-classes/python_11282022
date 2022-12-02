import csv
import itertools


with open('cities.csv', encoding="UTF-8") as csvfile:

    csvreader = csv.DictReader(csvfile)

    for row in itertools.islice(csvreader, 0, 5):
        print(row)
