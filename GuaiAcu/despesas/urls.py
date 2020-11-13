from django.urls import path

from GuaiAcu.despesas import views

app_name = 'despesas'

urlpatterns = [
    path('', views.despesas, name='despesas'),
]
