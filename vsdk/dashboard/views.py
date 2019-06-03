from django.shortcuts import render
from django.http import HttpResponse

from collections import OrderedDict

from vsdk.dashboard.fusioncharts import FusionCharts

from vsdk.service_development.models import UserInput, session, user, dashboard_input

from datetime import datetime
import time
from collections import OrderedDict

def Chart(request):

#####barchart#####
    dataSourceBar = {}
    dataSourceBar['chart'] = {
        "caption": "Rainfall",
            "subCaption": "Shown per date",
            "xAxisName": "Session",
            "yAxisName": "Rainfall in MM",
            "theme": "Gammel",
        }

    dataSourceBar['data'] = []	
		
    objects_with_category_id_2 = dashboard_input.objects.filter(service_service_id=3,category_category_id=2)

    for obj in objects_with_category_id_2:
        data =  {'label': obj.session_start.strftime("%m.%Y"),
                 'value': obj.input_input_value}
        dataSourceBar['data'].append(data)	
 
#####Donut#####
    dataSourcePie = {}
    dataSourcePie['chart'] = {
        "caption": "Farmers and their input",
        "subCaption" : "How much have farmers submittted their data",
        "showValues":"0",
        "showPercentInTooltip" : "1",
        "enableMultiSlicing":"1",
        "enableSmartLabels": "1",
        "smartLineColor": "#0c0404",
        "smartLineThickness": "1",
        "smartLineAlpha": "50",
        "isSmartLineSlanted": "1",
        "skipOverlapLabels": "1",
        "theme": "Gammel"
        }

    dataSourcePie['data'] = []	    
		
    objects_with_category_id_1 = dashboard_input.objects.filter(service_service_id=3,category_category_id=1)



    for obj in objects_with_category_id_1:
        data =  {'label': obj.farmer_id, 
                 'value': obj.input_input_value}# change to count input row
        dataSourcePie['data'].append(data)	

	
##Render	
    doughnut3d = FusionCharts("doughnut3d", "PIE" , "100%", "400", "pie-container", "json", dataSourcePie)	
    column2D = FusionCharts("column3d", "BAR" , "600", "400", "Barchart-container", "json", dataSourceBar)
    return  render(request, 'dash.html', {'output' : column2D.render(),'output2' : doughnut3d.render()})