import csv

with open('names.csv', 'w', encoding="UTF-8") as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Bob', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Joan', 'last_name': 'Thomas'})
    writer.writerow({'first_name': 'Tim', 'last_name': 'Timmons'})
