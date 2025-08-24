from django.http import HttpResponse


def car_view(request):
    return HttpResponse('Meus carros') 
