from rest_framework import serializers

from .models import Bill


class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'
