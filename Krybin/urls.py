from django.urls import path
from .views import home, final_view

urlpatterns = [
    path('krybin/', home),
    path('krybin/<str:slugs>', final_view),
]