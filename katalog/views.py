from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    getCatalogs = CatalogItem.objects.all()
    context = {
        'Name' : 'Alizha',
        'Student_ID' : '2106652000',
        'catalogs' : getCatalogs
    }

    return render(
        request,
        'katalog.html',
        context
    )
