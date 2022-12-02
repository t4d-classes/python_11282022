import csv

with open('names2.csv', 'w', encoding="UTF-8") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['first_name', 'last_name'])
    writer.writerow(['Bob', 'Smith'])
    writer.writerow(['Joan', 'Thomas'])
    writer.writerow(['Tim', 'Timmons'])
