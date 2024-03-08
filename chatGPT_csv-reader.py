import csv

with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Ausschneiden des ersten Feldes in Anführungszeichen
        first_field = row[0].strip('"')
        print("Erstes Feld:", first_field)

        # Bearbeiten der aktuellen Zeile ab hier
        # ...
