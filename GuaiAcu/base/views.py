# Create your views here.
from django.shortcuts import render


def home(request):
    # raise ValueError() => for Sentry test
    # return HttpResponse('<html><body>Olá Django</body></html>', content_type='text/html')
    return render(request, 'base/home.html')
