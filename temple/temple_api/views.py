from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
import json
import requests
import re
import csv
# Create your views here.
class GetTempleAPIView(APIView):
    def post(self,request, format=None):
        body = request.body
        body_load = json.loads(body)
        body_list = body_load["body"]
        print(body_list)
        provinces = {
            "ROY": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดร้อยเอ็ด",
            "RAN": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดระนอง",
            "RAY": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดระยอง",
            "YAL": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดยะลา"
        }
        all_temple_list = []
        for p in body_list:
            print(p)
            data = requests.get(provinces[p])
            pattern = r'<div id="mw-content-text" class="mw-body-content.*id="ดูเพิ่ม">ดูเพิ่ม</span>'
            result = re.findall(pattern, data.text,flags=re.DOTALL | re.MULTILINE)
            pattern = r'<li>.*</li>'
            result = re.findall(pattern,result[0] )
            result = re.sub('<.*?>','', '\n'.join(result))
            pattern = r'วัด.* '
            result = re.findall(pattern, result)
 
            result = re.sub(' (.*) ','','\n'.join(result))
            print(result)
            temples = result.split('\n')
            for temple in temples:
                all_temple_list.append(temple)
            print(all_temple_list)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="templev1.csv.csv"'
        writer = csv.writer(response, delimiter=' ')
        writer.writerows([[temple.replace("\"",'').replace(" ",'')] for temple in all_temple_list])
        return response