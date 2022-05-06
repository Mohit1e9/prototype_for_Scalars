from django.shortcuts import render
from django.views import View
from Screen_02.views.utilities import fetchISOFromAPI
from Screen_02.views.utilities import (
    textFormatter,
    dataFrameBuilder,
    fetchNodesFromAPI,
    fetchISOFromAPI,
)
from Screen_01.Utilities import finalScalar

import requests


class Prototype_02(View):
    templateName = "Prototype_02.html"
    months = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    ISOname = fetchISOFromAPI()
    scalar = {"Months": months, "Hours": range(1, 25), "ISO": ISOname}

    def get(self, request, iso_name=None, nodes=None):
        if iso_name and nodes:
            paramters = {
                "startdate": "2022-04-01T00:00:00",
                "enddate": "2022-04-12T01:00:00",
                "data_format": "json",
            }

            data_column = ["da_price", "rt_price"]
            months = [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
                "Jul",
                "Aug",
                "Sep",
                "Oct",
                "Nov",
                "Dec",
            ]

            urlForNodeData = "https://berlin.enine.dev/api/v1/spider/data/{iso}/node/{node}/{data_column}".format(
                iso=iso_name, node=nodes, data_column=self.data_column[0]
            )

            response = requests.get(url=urlForNodeData, params=self.paramters)

            if response.status_code == 200:
                print("API call successful with parameters")
                JSONParsedDictionary = textFormatter(response.content)
                dataFrameBuilder(JSONParsedDictionary)
                # Scalars['weekday']=finalScalar()['weekday']
                # Scalars['weekend']=finalScalar()['weekend']
                # Scalars['months']=finalScalar()['Months']
                # scalar=finalScalar()
                scalar = {
                    "Months": self.months,
                    "Hours": range(1, 25),
                    "weekday": finalScalar()["weekday"],
                    "weekend": finalScalar()["weekend"],
                    "ISO": iso_name,
                }
                return render(request, "Prototype_02.html", scalar)
                # return JsonResponse(scalar,safe=False)
            else:
                print(f"Status code {response.status_code}")

        return render(request, self.templateName, self.scalar)
