from django.urls import path
from .views import url_home, final_routing

urlpatterns = [
    path('ShortIT/', url_home),
    path('<str:finish_id>', final_routing)
    ]