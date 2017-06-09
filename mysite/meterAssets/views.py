from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Meter

# Create your views here.
def index(request):
    return HttpResponse("It's Working")

def meter_data_list(request):
    meters = Meter.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'meterAssets/meter_data_list.html', {'meters' : meters})
    