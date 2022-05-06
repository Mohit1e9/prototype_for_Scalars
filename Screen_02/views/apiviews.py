import requests

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from Screen_02.views.utilities import textFormatter,dataFrameBuilder,fetchNodesFromAPI,fetchISOFromAPI
from Screen_01.Utilities import finalScalar
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
   
    return dictionary.get(key)

class getNodesFromISO(View):
    
    def get(self,request,iso_name):
           
        nodes=fetchNodesFromAPI(iso_name)
       
        return JsonResponse(nodes,safe=False)

class getDataFromISONode(View):
    paramters={
        "startdate":"2022-04-01T00:00:00",
        "enddate":"2022-04-12T01:00:00",
        "data_format":"json"
    }
    
    data_column=["da_price","rt_price"]
    months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    def get(self,request,iso_name,nodes):
                
        urlForNodeData="https://berlin.enine.dev/api/v1/spider/data/{iso}/node/{node}/{data_column}".format(iso=iso_name,node=nodes,data_column=self.data_column[0])

        response=requests.get(url=urlForNodeData,params=self.paramters)
        
        if response.status_code==200:
            print("API call successful with parameters")
            JSONParsedDictionary=textFormatter(response.content)
            dataFrameBuilder(JSONParsedDictionary)
            # Scalars['weekday']=finalScalar()['weekday']
            # Scalars['weekend']=finalScalar()['weekend']
            # Scalars['months']=finalScalar()['Months']
            #scalar=finalScalar()
            scalar={
                "Months":self.months,
                "Hours":range(1,25),
                "weekday":finalScalar()['weekday'],
                "weekend":finalScalar()['weekend'],
                "ISO":iso_name

                }
            return render(request,"Prototype_02.html",scalar)
            #return JsonResponse(scalar,safe=False)
        else:
            print(f"Status code {response.status_code}")