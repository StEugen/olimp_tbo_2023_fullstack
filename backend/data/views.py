import csv, os

from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from data.serializers import UserSerializer


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


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(
            username=username, password=password
        )

        if user:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
