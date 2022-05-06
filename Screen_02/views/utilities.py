import pandas as pd
import json,requests

def dateTimeMerger(deliverydate,hourending):
    result= deliverydate.split('T')[0] +" "+ hourending
    return result

def dataFrameBuilder(JSONParsedDictionary):
    resultdictionary={}  
    dateTimeList=[]
  
    for i in range(len(JSONParsedDictionary["deliverydate"])):
        dateTimeList.append(dateTimeMerger(JSONParsedDictionary["deliverydate"][i],JSONParsedDictionary["hourending"][i]))
        
    resultdictionary={"dtm":dateTimeList,"price":JSONParsedDictionary["settlementpointprice"]}
    scalarDataFrame=pd.DataFrame(resultdictionary)
    
    print(scalarDataFrame)

def textFormatter(obj):
        text=json.loads(obj)
        deliveryDateList,hourEndingList,settlePointPriceList=[],[],[]
        
        for i in range(len(text["data"])):
            deliveryDateList.append(text["data"][i]["deliverydate"])
            hourEndingList.append(text["data"][i]["hourending"])            
            settlePointPriceList.append(text["data"][i]["settlementpointprice"])
        
        JSONParsedDictionary={
        "deliverydate":deliveryDateList,
        "hourending":hourEndingList,
        "settlementpointprice":settlePointPriceList
        }        
        
        return JSONParsedDictionary

def fetchISOFromAPI():
    
    url="https://berlin.enine.dev/api/v1/spider/data/"
    print(url)
    response=requests.get(url)
    if response.status_code==200:
        print("Successful Call to Avalaible price nodes API")
        text=json.loads(response.content)
        ISOList=text["Data available for ISOs"]
        print(ISOList)
    else:
        print(f"Status code {response.status_code}")
    return ISOList


def fetchNodesFromAPI(ISO):
    
    url="https://berlin.enine.dev/api/v1/spider/data/{iso}/node/".format(iso=ISO)
    print(url)
    response=requests.get(url)
    if response.status_code==200:
        print("Successful Call to Avalaible price nodes API")
        text=json.loads(response.content)
        nodes=text["data"]
    else:
        print(f"Status code {response.status_code}")
    return nodes

"""
Cautionary note:Above this line is something for which you must recall the quote from Steve Jobs:
    If it is working,do not touch it!!!.
"""


#dateTimeMerger("2022-04-01T00:00:00Z","13:00")

# JSONParsedDictionary={
#     "deliverydate":["2022-04-01T00:00:00Z","2022-04-02T00:00:00Z","2022-04-03T00:00:00Z"],
#     "Hourending":["06:00","07:00","08:00"],
#     "Price":[40.46,22.29,21.29]
# }   