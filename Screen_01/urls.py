from django.urls import path

from Screen_01.views.appviews import Prototype_01

urlpatterns=[
      path('PrototypeScreen/', Prototype_01.as_view()),
      
]