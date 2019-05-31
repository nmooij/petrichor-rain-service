from django.shortcuts import render
from django.http import HttpResponse


from collections import OrderedDict

# Include the `fusioncharts.py` file that contains functions to embed the charts.
#from fusioncharts import FusionCharts
from vsdk.dashboard.fusioncharts import FusionCharts

#from ..models import *
from vsdk.service_development.models import UserInput, session

from datetime import datetime
import time

def myFirstChart(request):

    dataSource = {}
    dataSource['chart'] = {
        "caption": "Rainfall",
            "subCaption": "Petrichor Rain Service",
            "xAxisName": "Session",
            "yAxisName": "Rainfall in MM",
            "numberPrefix": "",
            "theme": "gammel"
        }

    dataSource['data'] = []


    objects_with_category_id_2 = UserInput.objects.filter(category_id=2)

    for obj in objects_with_category_id_2:
        data =  {'label': obj.input_description, #TO DO CHANGE TO DATE
                 'value': obj.input_value}
        dataSource['data'].append(data)	

          
    # #Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    # dataSource = OrderedDict()

    # # The `chartConfig` dict contains key-value pairs of data for chart attribute
    # chartConfig = OrderedDict()
    # chartConfig['caption'] = 'Countries With Most Oil Reserves [2017-18]'
    # chartConfig['subCaption'] = 'In MMbbl = One Million barrels'
    # chartConfig['xAxisName'] = 'Country'
    # chartConfig['yAxisName'] = 'Reserves (MMbbl)'
    # chartConfig['numberSuffix'] = 'K'
    # chartConfig['theme'] = 'fusion'

    # # The `chartData` dict contains key-value pairs of data
    # chartData = OrderedDict()
    # chartData['Venezuela'] = 290
    # chartData['Saudi'] = 260
    # chartData['Canada'] = 180
    # chartData['Iran'] = 140
    # chartData['Russia'] = 115
    # chartData['UAE'] = 100
    # chartData['US'] = 30
    # chartData['China'] = 30
    # chartData['Spain'] = 49

    # dataSource['chart'] = chartConfig
    # dataSource['data'] = []

    # # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    # #The data for the chart should be in an array wherein each element of the array
    # #is a JSON object# having the `label` and `value` as keys.

    # #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    # for key, value in chartData.items():
        # data = {}
    # data['label'] = key
    # data['value'] = value
    # dataSource['data'].append(data)


# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "ex1" , "600", "400", "myFirstchart-container", "json", dataSource)

    return  render(request, 'dash.html', {'output' : column2D.render(), 'chartTitle': 'Simple Chart Using Array'})