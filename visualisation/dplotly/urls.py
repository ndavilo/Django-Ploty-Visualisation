from django.urls import path
from .views import UploadCSV, Home

urlpatterns = [
    path('', Home, name='home'),
    path('uploadcsv', UploadCSV, name='uploadcsv')
]