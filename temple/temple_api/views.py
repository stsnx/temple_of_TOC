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

    def _get_province(self):
        provinces = {
            "ROY": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดร้อยเอ็ด",
            "RAN": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดระนอง",
            "RAY": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดระยอง",
            "YAL": "https://th.wikipedia.org/wiki/รายชื่อวัดในจังหวัดยะลา"
        }
        return provinces

    def post(self,request, format=None):
        body = request.body
        body_load = json.loads(body)
        body_list = body_load["body"]
        print(body_list)
        provinces = self._get_province()
        all_temple_list = []
        for p in body_list:
            print(p)
            data = requests.get(provinces[p])
            pattern = r'<div id="mw-content-text" class="mw-body-content.*id="ดูเพิ่ม">ดูเพิ่ม</span>'
            result = re.findall(pattern, data.text,flags=re.DOTALL | re.MULTILINE)
            pattern = r'<li>.*</li>'
            result = re.findall(pattern,result[0] )
            result = re.sub('<.*?>','', '\n'.join(result))
            pattern = r'วัด.*'
            result = re.findall(pattern, result)
            result = re.sub(' .*','','\n'.join(result))
            print(result)
            temples = result.split('\n')
            for temple in temples:
                all_temple_list.append(temple)
            print(all_temple_list)
        all_temple_list_ex_dup = []
        for temple in all_temple_list:
            if temple not in all_temple_list_ex_dup:
                all_temple_list_ex_dup.append(temple)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="templev1.csv.csv"'
        writer = csv.writer(response, delimiter=' ')
        writer.writerows([[temple.replace("\"",'').replace(" ",'')] for temple in all_temple_list_ex_dup])
        return response
    
    def get(self,request):
        query_province = request.GET.get('p', '').split(',')
        print(query_province)
        provinces = self._get_province()
        temples_obj = {}
        for p in query_province:
            all_temple_list = []
            print(p)
            data = requests.get(provinces[p])
            pattern = r'<div id="mw-content-text" class="mw-body-content.*id="ดูเพิ่ม">ดูเพิ่ม</span>'
            result = re.findall(pattern, data.text,flags=re.DOTALL | re.MULTILINE)
            pattern = r'<li>.*</li>'
            result = re.findall(pattern,result[0] )
            result = re.sub('<.*?>','', '\n'.join(result))
            pattern = r'วัด.*'
            result = re.findall(pattern, result)
            result = re.sub(' .*','','\n'.join(result))
            print(result)
            temples = result.split('\n')
            for temple in temples:
                all_temple_list.append(temple)
            print(all_temple_list)
            temples_obj[p] = all_temple_list
        temple_obj_removed_dup = {}
        for province in temples_obj.items():
            _l = []
            p = list(province)
            for temple in p[1]:
                if temple not in _l:
                    _l.append(temple)
            temple_obj_removed_dup[p[0]] = _l
        responseData = {}
        responseData["status"] = 200
        responseData["data"] = temple_obj_removed_dup
        response = HttpResponse(content_type='application/json',content=json.dumps(responseData))
        return response