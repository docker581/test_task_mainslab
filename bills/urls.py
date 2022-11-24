from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import UploadFileView, BillListView

router = DefaultRouter()
urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('bills/', BillListView.as_view(), name='bills'),
]
urlpatterns += router.urls
