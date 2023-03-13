from django.shortcuts import render
import csv, os
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from data.serializers import UserSerializer
from django.contrib.auth.models import User


current_dir = os.path.abspath(os.path.dirname(__file__))


class DataViewset(viewsets.ViewSet):
    """ Sends csv file to user """
    def list(self, request):
        data_file = os.path.join(current_dir, 'csvFiles', 'data-structure.csv')
        data = extract_data_csv(data_file)
        return JsonResponse(data, safe=False)

def extract_data_csv(filename, header_row=0):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        head = next(reader)
        for i, row in enumerate(reader):
            if i == head:
                continue 
            record = {}
            for col_index, col_name in enumerate(head):
                if col_index < len(row):
                    record[col_name] = row[col_index]
                else:
                    record[col_name] = None
            data.append(record)
    return data



def upload_file(file):
    pass






class UserCreateViewset(viewsets.ViewSet):
    """ Sends csv file to user """
    def create_user(self, request):
        return JsonResponse({ "status": "ok"}, safe=False)