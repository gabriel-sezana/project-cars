from django.shortcuts import render


def car_view(request):
    return render(request, 'cars.html')
