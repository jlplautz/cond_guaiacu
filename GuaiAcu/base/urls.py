from django.urls import path, include
from GuaiAcu.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('despesas/', include('GuaiAcu.despesas.urls')),
]
