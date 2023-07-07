from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from services import get_data, get_frameworks
from datetime import datetime


def data(request):
    data = get_data()
    return JsonResponse(status=200, data=data.__dict__)


def list(request):
    data = {
        "responseCode": 0,
        "message": "process ok",
        "data": get_frameworks(),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return JsonResponse(status=200, data=data)
