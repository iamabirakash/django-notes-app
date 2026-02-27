from django.urls import path
from .views import *
urlpatterns = [
    path('', indexView, name="land"),
    path('about/', about, name="about"),
    path('save/', save_data, name='save_data'),
    path('delete/<int:id>/', deleteView, name='delete'),
    path('edit/<int:id>/', editView, name='edit'),
]
