from django.shortcuts import render
from django.http import HttpResponse

from vsdk.dashboard.fusioncharts import FusionCharts

from vsdk.service_development.models import UserInput, session, user, dashboard_input
from vsdk.dashboard.models import AvgRainPerCountry

from datetime import datetime
import time
from datetime import date
from collections import OrderedDict



def Chart(request):

#####barchart#####
    dataSourceBar = {}
    dataSourceBar['chart'] = {
        "caption": "Rainfall",
            "subCaption": "Shown per date",
            "xAxisName": "Month",
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



    doughnut3d = FusionCharts("doughnut3d", "PIE" , "100%", "400", "pie-container", "json", dataSourcePie)	
    column2D = FusionCharts("column3d", "BAR" , "600", "400", "Barchart-container", "json", dataSourceBar)


##Line
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

    now = date.today()
    this_month = datetime.now().strftime("%m") #this_month = datetime.now().strftime("%B")
    this_year = datetime.now().strftime("%Y")
    this_day = datetime.now().strftime("%d")
	
	
	
    # sum = 0
    # input_input_value_with_category_id_2 = dashboard_input.objects.filter(service_service_id=3,category_category_id=2).values('input_input_value')
    # for value in input_input_value_with_category_id_2:
	    # sum += value


    #Rain_this_month = sum
    #Rain_this_year = 
	
	
##Historic_rain_this_month 
    if datetime.now().strftime("%B") == 'January':
        Historic_rain_this_month = 366676
    elif datetime.now().strftime("%B") == 'February':
        Historic_rain_this_month = 309590
    elif datetime.now().strftime("%B") == 'March':
        Historic_rain_this_month = 578333
    elif datetime.now().strftime("%B") == 'April':
        Historic_rain_this_month = 361117
    elif datetime.now().strftime("%B") == 'May':
        Historic_rain_this_month = 161616
    elif datetime.now().strftime("%B") == 'June':
        Historic_rain_this_month = 178011
    elif datetime.now().strftime("%B") == 'July':
        Historic_rain_this_month = 261100
    elif datetime.now().strftime("%B") == 'Augustus':
        Historic_rain_this_month = 347110
    elif datetime.now().strftime("%B") == 'September':
        Historic_rain_this_month = 170168
    elif datetime.now().strftime("%B") == 'October':
        Historic_rain_this_month = 265677
    elif datetime.now().strftime("%B") == 'November':
        Historic_rain_this_month = 413062
    elif datetime.now().strftime("%B") == 'December':
        Historic_rain_this_month = 277110
    else:
        Historic_rain_this_month = 0
	
##Histori_rain_this_year 
    if datetime.now().strftime("%B") == 'January':
        Histori_rain_this_year = 366676
    elif datetime.now().strftime("%B") == 'February':
        Histori_rain_this_year = 676266
    elif datetime.now().strftime("%B") == 'March':
        Histori_rain_this_year = 1254599
    elif datetime.now().strftime("%B") == 'April':
        Histori_rain_this_year = 1615716
    elif datetime.now().strftime("%B") == 'May':
        Histori_rain_this_year = 1777332
    elif datetime.now().strftime("%B") == 'June':
        Histori_rain_this_year = 1955343
    elif datetime.now().strftime("%B") == 'July':
        Histori_rain_this_year = 2216443
    elif datetime.now().strftime("%B") == 'Augustus':
        Histori_rain_this_year = 2563553
    elif datetime.now().strftime("%B") == 'September':
        Histori_rain_this_year = 2733721
    elif datetime.now().strftime("%B") == 'October':
        Histori_rain_this_year = 2999398
    elif datetime.now().strftime("%B") == 'November':
        Histori_rain_this_year = 3412460
    elif datetime.now().strftime("%B") == 'December':
        Histori_rain_this_year = 3689570
    else:
        Histori_rain_this_year = 0	

    mapbox_access_token = "'pk.eyJ1Ijoic3R1ZGVudG5hdGFzamEiLCJhIjoiY2p4M2IxNDhvMDF2aTQ0cDlpMm13dWVubyJ9.iiGzFV2EbEYh0_KIZAfs-w'"
	
	
    context = {
        'output' : column2D.render(),
        'output2' : doughnut3d.render(),
        'output3' : area2D.render(),
        #'Rain_this_month': Rain_this_month,
        #'Rain_this_year': Rain_this_year,
        'this_year': this_year,
        'this_month': this_month,
		'this_day': this_day,
        'Historic_rain_this_month': Historic_rain_this_month,
        'Histori_rain_this_year': Histori_rain_this_year,
        'mapbox_access_token': mapbox_access_token
    }
    return  render(request, 'dash.html', context)
	