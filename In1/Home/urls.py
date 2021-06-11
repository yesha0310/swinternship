from django.urls import path
from .views import home1

app_name="Home"

urlpatterns = [
    path('',home1,name="Home"),
]
