from django.urls import path
from mywatchlist.views import show_json_by_id, show_mywatchlist, show_xml_by_id
from mywatchlist.views import show_xml
from mywatchlist.views import show_json

app_name =  'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name = 'show_mywatchlist'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name = 'show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name = 'show_json_by_id'),
]