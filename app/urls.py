from django.urls import path
from .views import ListView,DetailView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/',ListView.as_view()),
    path('api/<int:pk>/',DetailView.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)