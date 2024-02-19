from django.urls import path
from users.views import dashbaord

urlpatterns = [
    path('dashboard/', dashbaord, name="dashboard"),
]
