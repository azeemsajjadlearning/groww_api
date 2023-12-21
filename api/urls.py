from django.urls import path
from api import views

urlpatterns = [
    path("get-popular-funds", views.get_popular_funds),
    path("get-meta-data", views.get_meta_data),
]
