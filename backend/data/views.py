from django.shortcuts import render
import csv 
from django.http import JsonResponse
from rest_framework import viewsets
import os

current_dir = os.path.abspath(os.path.dirname(__file__))


class DataViewset(viewsets.ViewSet):
    def list(self, request):
        data_file = os.path.join(current_dir, 'csvFiles', 'data-structure.csv')
        data = extract_data_csv(data_file)
        return JsonResponse(data, safe=False)

def extract_data_csv(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        id_col = header.index('id:')
        name_col = header.index('Название:')
        name_eng = header.index('Название (in english):')
        active = header.index('Активный:')
        description = header.index('Краткое описание:')
        long_description = header.index('Детальное описание:')
        description_eng = header.index(
            'Краткое описание (in english):'
            )
        long_description_eng = header.index(
            'Детальное описание (in english):'
            )
        mo = header.index('МО:')
        federal_subject = header.index('Субъект федерации:')
        significance = header.index('Значимость:')
        place = header.index('Населенный пункт:')
        place_eng = header.index('Населенный пункт (in english):')
        Address = header.index('Адрес:')
        Address_eng = header.index('Адрес (in english):')

        for row in reader:
            id_value = row[id_col]
            name_value = row[name_col]
            data.append({
                "id": id_value,
                "name": name_value,

            })
    return data


def upload_file(file):
    pass


