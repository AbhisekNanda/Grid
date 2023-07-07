from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.serializers import serialize
import json

# Create your views here.
@api_view(['POST'])
def search(request):

    search = request.data
    
    search_data = User.objects.filter(first_name__contains = search['search'])

    d=serialize("json", search_data)
    json_data=json.loads(d)
    
    json_fields=[i['fields'] for i in json_data]

    return Response(
        {
            "Data":json.loads(json.dumps(json_fields))
        }
    )
            
  
        
