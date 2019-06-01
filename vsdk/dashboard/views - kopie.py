from django.shortcuts import render
from django.http import HttpResponse

from collections import OrderedDict

from vsdk.dashboard.fusioncharts import FusionCharts

from vsdk.service_development.models import UserInput, session

from datetime import datetime
import time
from collections import OrderedDict

def Chart(request):

    dataSourceBar = {}
    dataSourceBar['chart'] = {
        "caption": "Rainfall",
            "subCaption": "Petrichor Rain Service",
            "xAxisName": "Session",
            "yAxisName": "Rainfall in MM",
            "numberPrefix": "",
            "theme": "gammel"
        }

    dataSourceBar['data'] = []

    objects_with_category_id_2 = UserInput.objects.filter(category_id=2)

    for obj in objects_with_category_id_2:
        data =  {'label': obj.input_description, #TO DO CHANGE TO DATE
                 'value': obj.input_value}
        dataSourceBar['data'].append(data)	

    column2D = FusionCharts("column2d", "BAR" , "600", "400", "Barchart-container", "json", dataSourceBar)

    return  render(request, 'dash.html', {'output' : column2D.render()})


    doughnut3d = FusionCharts("doughnut3d", "ex2" , "100%", "400", "pie-container", "json", 

    """{ 
        "chart": {
            "caption": "Recommended Portfolio Split",
            "subCaption" : "For a net-worth of $1M",
            "showValues":"1",
            "showPercentInTooltip" : "0",
            "numberPrefix" : "$",
            "enableMultiSlicing":"1",
            "enableSmartLabels": "1",
            "smartLineColor": "#0c0404",
            "smartLineThickness": "1",
            "smartLineAlpha": "50",
            "isSmartLineSlanted": "1",
            "skipOverlapLabels": "1",
            "theme": "fusion",

        },
		
		dataSource['data'] = []
    
        for key in UserInput.objects.all():
            data = [{}]
            data['label'] = key.input_description
            data['value'] = key.input_value
            dataSource['data'].append(data)
		
		
        "data": [{
            "label": "Equity",
            "value": "300000"
        }, {
            "label": "Debt",
            "value": "230000"
        }, {
            "label": "Bullion",
            "value": "180000"
        }, {
            "label": "Real-estate",
            "value": "270000"
        }, {
            "label": "Insurance",
            "value": "20000"
        }]
		
		
    }""")
  
    return  render(request, 'dash.html', {'output2' : doughnut3d.render(), 'chartTitle': 'Pie 3D Chart'})


    dataSourceMap = OrderedDict()
    mapConfig = OrderedDict()
    mapConfig["caption"] = "Average Annual Population Growth"
    mapConfig["subcaption"] = "1955-2015"
    mapConfig["numbersuffix"] = "%"
    mapConfig["includevalueinlabels"] = "1"
    mapConfig["labelsepchar"] = ":"
    mapConfig["theme"] = "fusion"

    colorDataObj = { "minvalue": "0", "code" : "#FFE0B2", "gradient": "1",    
      "color" : [
          { "minValue" : "0.5", "maxValue" : "1", "code" : "#FFD74D" },
          { "minValue" : "1.0", "maxValue" : "2.0", "code" : "#FB8C00" },
          { "minValue" : "2.0", "maxValue" : "3.0", "code" : "#E65100" }
      ]
    }

    dataSourceMap["chart"] = mapConfig
    dataSourceMap["colorrange"] = colorDataObj
    dataSourceMap["data"] = []

    mapDataArray = [
      ["NA", "0.82", "1"],
      ["SA", "2.04", "1"],
      ["AS", "1.78", "1"],
      ["EU", "0.40", "1"],
      ["AF", "2.58", "1"],
      ["AU", "1.30", "1"]
    ]

    for i in range(len(mapDataArray)):        
        dataSourceMap["data"].append({"id": mapDataArray[i][0], "value": mapDataArray[i][1], "showLabel": mapDataArray[i][2] })

    fusionMap = FusionCharts("maps/world", "MAP" , "650", "450", "Map-container", "json", dataSourceMap)

    return  render(request, 'dash.html', {'output3' : fusionMap.render()})
   