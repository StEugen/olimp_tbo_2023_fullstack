import csv
from ..data.models import Csvdata

with open('mycsvfile.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Csvdata.objects.create(
            id=row['id'],
            name=row['Название:'],
            name_english=row['Название (in english):'],
            is_active=row['Активный:'] == 'да',
            # Add more fields here to match the columns in your CSV file
        )

