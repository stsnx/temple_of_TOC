from django.urls import path
from . import views
from django.urls import path
urlpatterns = [
    path('gettemple/',views.GetTempleAPIView.as_view()),
]