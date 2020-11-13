from django.shortcuts import render


# Create your views here.
def despesas(request):
    return render(request, 'despesas/index.html')
