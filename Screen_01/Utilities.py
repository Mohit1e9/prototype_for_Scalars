import random
from token import TYPE_IGNORE
import pandas as pd
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    print(dictionary.get(key))
    return dictionary.get(key)

def randomPeakhour():
    peakhourConsumption= int(16)
    hourlyConsumption=[]
    for i in range(peakhourConsumption):
        if(peakhourConsumption>=0):
            randomPeakhourScalar=random.uniform(0,peakhourConsumption)
            peakhourConsumption=peakhourConsumption-randomPeakhourScalar

        hourlyConsumption.append(round(randomPeakhourScalar,2))
        i=i+1
    
    return hourlyConsumption
   

def randomOffpeak():
    offpeakConsumption= int(8)
    hourlyConsumption=[]
    for i in range(offpeakConsumption):
        if(offpeakConsumption>=0):
            randomOffpeakScalar=random.uniform(0,offpeakConsumption)
            offpeakConsumption=offpeakConsumption-randomOffpeakScalar

        hourlyConsumption.append(round(randomOffpeakScalar,2))
        i=i+1
   
    return hourlyConsumption
    
def monthScalarValues():
    resultOffPeak,resultPeakHour = randomOffpeak(),randomPeakhour()
    finalScalarResult=[]
    finalScalarResult.extend(resultOffPeak[:6])
    finalScalarResult.extend(resultPeakHour)
    finalScalarResult.extend(resultOffPeak[6:])
    #print(finalScalarResult,len(finalScalarResult))
    return finalScalarResult
    
def readExcelForNodes():
    
    df=pd.read_excel(r"/home/curiosity/Desktop/frontend/Node_to_hub_ercot.xlsx")
    nodes=df['Node'].to_list()
    numberOfNodes=len(nodes)
    random.shuffle(nodes)
    numberOfNode=random.randint(1,numberOfNodes)
    return nodes[:numberOfNode]

def finalScalar():
    print("GET SCALARS")
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
    print("Scalar: ", type(Scalars))
    return Scalars
   