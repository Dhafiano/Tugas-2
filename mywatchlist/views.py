from django.shortcuts import render
from mywatchlist.models import BarangWatchList
from django.http import HttpResponse
from django.core import serializers

def mywatchlist(request):
    data_watchlist = BarangWatchList.objects.all()
    context = {
    'list_watchlist': data_watchlist,
    'name': 'Dhafiano Fadeyka Ghani Wiweko',
    'studentid': '2106751631'
    }
    return render(request, "watchlist.html", context)

def show_xml(request):
    data = BarangWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = BarangWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
