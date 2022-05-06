import pandas as pd
import json, requests


def dateTimeMerger(deliverydate, hourending):
    result = deliverydate.split("T")[0] + " " + hourending
    return result


def dataFrameBuilder(JSONParsedDictionary):
    resultdictionary = {}
    dateTimeList = []

    for i in range(len(JSONParsedDictionary["deliverydate"])):
        dateTimeList.append(
            dateTimeMerger(
                JSONParsedDictionary["deliverydate"][i],
                JSONParsedDictionary["hourending"][i],
            )
        )

    resultdictionary = {
        "dtm": dateTimeList,
        "price": JSONParsedDictionary["settlementpointprice"],
    }
    scalarDataFrame = pd.DataFrame(resultdictionary)

    print(scalarDataFrame)


def textFormatter(obj, data_coloumn):
    text = json.loads(obj)
    if data_coloumn=="da_price":
        deliveryDateList, hourEndingList, settlePointPriceList = [], [], []

        for i in range(len(text["data"])):
            deliveryDateList.append(text["data"][i]["deliverydate"])
            hourEndingList.append(text["data"][i]["hourending"])
            settlePointPriceList.append(text["data"][i]["settlementpointprice"])

        JSONParsedDictionary = {
            "deliverydate": deliveryDateList,
            "hourending": hourEndingList,
            "settlementpointprice": settlePointPriceList,
        }

        return JSONParsedDictionary
    
def foo(text):
    
    for i in range(len(text["data"])):
        lmp_List,sced_time_stamp_date_List,sced_time_stamp_hour_List=[],[],[]
        price=text["data"][i]["lmp"]
        sced_time_stamp_date,sced_time_stamp_hour=text["data"][i]["scedtimestamp"].split("T")[0],text["data"][i]["scedtimestamp"].split("T")[1].split("Z")[0]
        sced_hour=sced_time_stamp_hour.split(":")[0]
        print(sced_time_stamp_date,sced_time_stamp_hour,sced_hour,len(sced_time_stamp_date),len(sced_time_stamp_hour))
        
        next_data_point=i+1
        while(sced_hour==sced_time_stamp_hour.split(":")[next_data_point]):
            pass
            
        




def fetchISOFromAPI():

    url = "https://berlin.enine.dev/api/v1/spider/data/"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print("Successful Call to Avalaible price nodes API")
        text = json.loads(response.content)
        ISOList = text["Data available for ISOs"]
        print(ISOList)
    else:
        print(f"Status code {response.status_code}")
    return ISOList


def fetchNodesFromAPI(ISO):

    url = "https://berlin.enine.dev/api/v1/spider/data/{iso}/node/".format(iso=ISO)
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print("Successful Call to Avalaible price nodes API")
        text = json.loads(response.content)
        nodes = text["data"]
    else:
        print(f"Status code {response.status_code}")
    return nodes


"""
Cautionary note:Above this line is something for which you must recall the quote from Steve Jobs:
    If it is working,do not touch it!!!.
"""


# dateTimeMerger("2022-04-01T00:00:00Z","13:00")

# JSONParsedDictionary={
#     "deliverydate":["2022-04-01T00:00:00Z","2022-04-02T00:00:00Z","2022-04-03T00:00:00Z"],
#     "Hourending":["06:00","07:00","08:00"],
#     "Price":[40.46,22.29,21.29]
# }

obj={
    "report": "LMPs by Resource Nodes, Load Zones and Trading Hubs",
    "source": "ERCOT",
    "data": [
        {
            "scedtimestamp": "2022-04-01T00:00:39Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 32.06,
            "recordtime": "2022-04-01 00:00:46"
        },
        {
            "scedtimestamp": "2022-04-01T00:15:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 45.99,
            "recordtime": "2022-04-01 00:15:18"
        },
        {
            "scedtimestamp": "2022-04-01T00:20:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 39.24,
            "recordtime": "2022-04-01 00:20:18"
        },
        {
            "scedtimestamp": "2022-04-01T00:25:15Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 36.38,
            "recordtime": "2022-04-01 00:25:19"
        },
        {
            "scedtimestamp": "2022-04-01T00:30:13Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 34.4,
            "recordtime": "2022-04-01 00:30:18"
        },
        {
            "scedtimestamp": "2022-04-01T00:35:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 33.25,
            "recordtime": "2022-04-01 00:35:21"
        },
        {
            "scedtimestamp": "2022-04-01T00:40:18Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 31.24,
            "recordtime": "2022-04-01 00:40:22"
        },
        {
            "scedtimestamp": "2022-04-01T00:45:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 30.79,
            "recordtime": "2022-04-01 00:45:19"
        },
        {
            "scedtimestamp": "2022-04-01T00:50:13Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 33.22,
            "recordtime": "2022-04-01 00:50:19"
        },
        {
            "scedtimestamp": "2022-04-01T00:55:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 32.78,
            "recordtime": "2022-04-01 00:55:20"
        },
        {
            "scedtimestamp": "2022-04-01T01:05:15Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 33.02,
            "recordtime": "2022-04-01 01:05:21"
        },
        {
            "scedtimestamp": "2022-04-01T01:10:15Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 34.31,
            "recordtime": "2022-04-01 01:10:20"
        },
        {
            "scedtimestamp": "2022-04-01T01:20:13Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 34.24,
            "recordtime": "2022-04-01 01:20:18"
        },
        {
            "scedtimestamp": "2022-04-01T01:25:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 32.13,
            "recordtime": "2022-04-01 01:25:24"
        },
        {
            "scedtimestamp": "2022-04-01T01:30:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 30.59,
            "recordtime": "2022-04-01 01:30:18"
        },
        {
            "scedtimestamp": "2022-04-01T01:35:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 26.08,
            "recordtime": "2022-04-01 01:35:20"
        },
        {
            "scedtimestamp": "2022-04-01T01:40:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 26.5,
            "recordtime": "2022-04-01 01:40:19"
        },
        {
            "scedtimestamp": "2022-04-01T01:45:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 23.5,
            "recordtime": "2022-04-01 01:45:24"
        },
        {
            "scedtimestamp": "2022-04-01T01:50:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 23.85,
            "recordtime": "2022-04-01 01:50:18"
        },
        {
            "scedtimestamp": "2022-04-01T01:55:13Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 27.73,
            "recordtime": "2022-04-01 01:55:20"
        },
        {
            "scedtimestamp": "2022-04-01T02:00:16Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 28.86,
            "recordtime": "2022-04-01 02:00:21"
        },
        {
            "scedtimestamp": "2022-04-01T02:05:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 25.83,
            "recordtime": "2022-04-01 02:05:19"
        },
        {
            "scedtimestamp": "2022-04-01T02:10:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 24.53,
            "recordtime": "2022-04-01 02:10:18"
        },
        {
            "scedtimestamp": "2022-04-01T02:15:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 25.92,
            "recordtime": "2022-04-01 02:15:18"
        },
        {
            "scedtimestamp": "2022-04-01T02:20:15Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 23.85,
            "recordtime": "2022-04-01 02:20:23"
        },
        {
            "scedtimestamp": "2022-04-01T02:25:15Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 28.26,
            "recordtime": "2022-04-01 02:25:20"
        },
        {
            "scedtimestamp": "2022-04-01T02:35:17Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 23.03,
            "recordtime": "2022-04-01 02:35:25"
        },
        {
            "scedtimestamp": "2022-04-01T02:40:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 22.46,
            "recordtime": "2022-04-01 02:40:18"
        },
        {
            "scedtimestamp": "2022-04-01T02:45:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 22.46,
            "recordtime": "2022-04-01 02:45:18"
        },
        {
            "scedtimestamp": "2022-04-01T02:50:15Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 22.45,
            "recordtime": "2022-04-01 02:50:23"
        },
        {
            "scedtimestamp": "2022-04-01T03:00:19Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 22.42,
            "recordtime": "2022-04-01 03:00:29"
        },
        {
            "scedtimestamp": "2022-04-01T03:05:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 22.41,
            "recordtime": "2022-04-01 03:05:21"
        },
        {
            "scedtimestamp": "2022-04-01T03:10:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 15.72,
            "recordtime": "2022-04-01 03:10:19"
        },
        {
            "scedtimestamp": "2022-04-01T03:15:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 7.88,
            "recordtime": "2022-04-01 03:15:18"
        },
        {
            "scedtimestamp": "2022-04-01T03:20:14Z",
            "repeatedhourflag": "N",
            "settlementpoint": "AEEC",
            "lmp": 6.66,
            "recordtime": "2022-04-01 03:20:20"
        }]
}
foo(obj)