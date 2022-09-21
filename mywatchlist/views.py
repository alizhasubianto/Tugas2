from django.shortcuts import render
from mywatchlist.models import watchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    getWatchList = watchList.objects.all()
    context = {
        'Name' : 'Alizha',
        'Student_ID' : '2106652000',
        'watchlist' : getWatchList
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = watchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = watchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")