from rest_framework import serializers
from csv_rest.models import Emloyee


class CsvOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emloyee
        fields = "__all__"
