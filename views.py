from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def data():
    return JsonResponse(status=200, data={"ResponseCode" : 0, "message": "Process OK"})


def list():
    return JsonResponse(status=200, data={"ResponseCode" : 0, "message": "Process OK"})