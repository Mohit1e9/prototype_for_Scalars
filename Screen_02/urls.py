from django.urls import path

from Screen_02.views.appviews import Prototype_02
from Screen_02.views.apiviews import getNodesFromISO,getDataFromISONode


urlpatterns=[
    path('PrototypeScreen/',Prototype_02.as_view()),
    path('PrototypeScreen/<str:iso_name>/<str:nodes>/',Prototype_02.as_view()),
    path('PrototypeScreen/prototype_02/<str:iso_name>/',getNodesFromISO.as_view()),
    path('PrototypeScreen/prototype_02/<str:iso_name>/<str:nodes>/',getDataFromISONode.as_view())
]