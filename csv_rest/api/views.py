from django.shortcuts import render
from rest_framework import generics, viewsets
import csv
from rest_framework.response import Response
from csv_rest.models import Emloyee
from csv_rest.api.serializers import CsvOperationSerializer
from rest_framework import status
from django.http import HttpResponse


class PostApiViewset(generics.CreateAPIView):
    queryset = Emloyee.objects.all()
    serializer_class = CsvOperationSerializer


class GetApiViewset(generics.ListAPIView):
    queryset = Emloyee.objects.all()
    serializer_class = CsvOperationSerializer


class UpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Emloyee.objects.all()
    serializer_class = CsvOperationSerializer


class DeleteApi(generics.DestroyAPIView):
    queryset = Emloyee.objects.all()
    serializer_class = CsvOperationSerializer


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['emp_id', 'firstname', 'lastname', 'email', 'profession'])

    users = Emloyee.objects.all().values_list('emp_id', 'firstname', 'lastname', 'email', 'profession')
    for user in users:
        writer.writerow(user)

    return response
