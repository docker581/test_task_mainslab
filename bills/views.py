from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Bill
from .serializers import UploadFileSerializer, BillSerializer
from .services import process_file_with_bills


class UploadFileView(generics.CreateAPIView):
    serializer_class = UploadFileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        process_file_with_bills(file)
        return Response({'status': 'success'}, status.HTTP_201_CREATED)


class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('client_org', 'client_name')
