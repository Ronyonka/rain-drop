import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect



from .models import *
from .forms import *



def home(request):
    today = datetime.date.today()
    startDate = request.GET.get('startDate', '2019-01-01')
    endDate = request.GET.get('endDate', '2020-01-01')
    if startDate > endDate:
        startDate , endDate = '2019-01-01', '2020-01-01'
    date_start = datetime.datetime.strptime(startDate, '%Y-%m-%d').date()
    date_end = datetime.datetime.strptime(endDate, '%Y-%m-%d').date()
    rain = Rain.objects.all()
    rain = Rain.my_query.get_queryset().filter_by_date(date_start, date_end)
    form = RainForm(request.POST)
    if request.method == 'GET':
        return render(request, 'main.html', {"rain":rain, "form":form})
    if request.method == "POST":
        if form.is_valid():
            if  Rain.objects.filter(date = form.cleaned_data['date']).exists():
                form = RainForm()
            elif form.cleaned_data['date'] > today:
                form = RainForm()
            else:
                form.save()
                return redirect('home')
        else:
            form = RainForm()
    return render(request, 'main.html', {'rain':rain, 'form': form})

