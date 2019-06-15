from django.shortcuts import render
from django.http import HttpResponse

from vsdk.dashboard.fusioncharts import FusionCharts

from vsdk.service_development.models import UserInput, session, user, dashboard_input
from vsdk.dashboard.models import AvgRainPerCountry

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
                 'value': obj.input_input_value}
        dataSourcePie['data'].append(data)	


##Line

    # dataSourceline = OrderedDict()

    # chartConfig = OrderedDict()
    # chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    # chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    # chartConfig["xAxisName"] = "Country"
    # chartConfig["yAxisName"] = "Reserves (MMbbl)"
    # chartConfig["theme"] = "fusion"


    # chartData = OrderedDict()
    # chartData["Jan"] = 366676
    # chartData["Feb"] = 309590
    # chartData["March"] = 578333
    # chartData["April"] = 361117
    # chartData["May"] = 161616
    # chartData["June"] = 178011
    # chartData["July"] = 261100
    # chartData["Aug"] = 347110
    # chartData["Sep"] = 170168
    # chartData["Oct"] = 265677
    # chartData["Nov"] = 413062
    # chartData["Dec"] = 277110

    # dataSourceline["chart"] = chartConfig
    # dataSourceline["data"] = []

    # for key, value in chartData.items():
        # data = {}
    # data["label"] = key
    # data["value"] = value
    # dataSourceline["data"].append(data)




##Render	
    doughnut3d = FusionCharts("doughnut3d", "PIE" , "100%", "400", "pie-container", "json", dataSourcePie)	
    column2D = FusionCharts("column3d", "BAR" , "600", "400", "Barchart-container", "json", dataSourceBar)

    area2D = FusionCharts("line", "AREA", "600", "400", "area-container", "json",
	
        """{
    "chart": {
        "caption": "Historic Rainfall",
        "subCaption": "Located in Ghana",
        "xAxisName": "Month",
        "yAxisName": "Rainfall in MM",
        "showValues": "1",
        "theme": "fusion"
    },
    "data": [
        {
            "label": "Jan",
            "value": "366676"
        },
        {
            "label": "Feb",
            "value": "309590"
        },
        {
            "label": "Mar",
            "value": "578333"
        },
        {
            "label": "April",
            "value": "361117"
        },
        {
            "label": "May",
            "value": "161616"
        },
        {
            "label": "June",
            "value": "178011"
        },
		{
            "label": "July",
            "value": "261100"
        },
		{
            "label": "Aug",
            "value": "347110"
        },
		{
            "label": "Sep",
            "value": "170168"
        },
		{
            "label": "Okt",
            "value": "265677"
        },
		{
            "label": "Nov",
            "value": "413062"
        },
        {
            "label": "Dec",
            "value": "277110"
        }
    ]
}""")
        


    return  render(request, 'dash.html', {'output' : column2D.render(),'output2' : doughnut3d.render(),'output3' : area2D.render()})



def view_name(request):
    now = datetime.datetime.now()
    today = 'heyy'#now.strftime("%A, %b %d, %Y")
    return render_to_response(request,'dash.html', {'today' : today.render()})