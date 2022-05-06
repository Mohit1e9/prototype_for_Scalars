from django.shortcuts import render
from Screen_01.Utilities import monthScalarValues,readExcelForNodes
from django.http import HttpResponse
from django.template.defaulttags import register
# Create your views here.
from django.views import View

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def Prototype_01():
    months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    iso=["ERCOT","CAISO","MISO","NYISO","ISONE","PJM","SPP"]
    weekdayDict,weekendDict,dropDownISONodes={},{},{}
    for i in range(len(months)):
        weekdayDict[months[i]]=monthScalarValues()
        weekendDict[months[i]]=monthScalarValues()
    
    for i in range(len(iso)):
        dropDownISONodes[iso[i]]=readExcelForNodes()

    Scalars={
        "Months":months,
        "Hours":range(1,25),
        "weekday":weekdayDict,
        "weekend":weekendDict,
        "ISONodes":dropDownISONodes
    }
    return Scalars

