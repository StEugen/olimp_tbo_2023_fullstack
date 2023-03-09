from django.shortcuts import render
import csv 
from django.http import JsonResponse

def extract_data_csv(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                'id': row[id]
            })
    return data


def data_view(request):
    data = extract_data_csv('./csvFiles/data-structure.csv')
    return JsonResponse(data, safe=False)

