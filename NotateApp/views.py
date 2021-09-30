from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from NotateApp.models import Txt

from NotateApp.serializers import TxtSerializer

from django.http.response import JsonResponse
from NotateApp.serializers import  TaggingSerializer


# Create your views here.

@csrf_exempt
def Txtapi(request,id=0):
    if request.method=='GET':
        txt = Txt.objects.all()
        txt_serializer = TxtSerializer(txt, many=True)
        return JsonResponse(txt_serializer.data, safe=False)
      
    elif request.method == 'POST':

        notate_data = JSONParser().parse(request)
        notate_Serializer = TaggingSerializer(data=notate_data)
        if notate_Serializer.is_valid():
            notate_Serializer.save()
            return JsonResponse("Adedd tag Successfully !", safe=False)
            return JsonResponse("failed  added tag ")
           


      