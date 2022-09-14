from django.shortcuts import render
from katalog.models import CatalogItem

def showkatalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_katalog,
    'name': 'Dhafiano Fadeyka Ghani Wiweko',
    'studentid': ''
}
    return render(request, "katalog.html", context)
# TODO: Create your views here.
