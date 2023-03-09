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
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                "id": row["id"],
            })
    return 



