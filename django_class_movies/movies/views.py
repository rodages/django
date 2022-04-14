from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def get_movie(request):
    return JsonResponse({"name":"The Prestige", "rating":"5"})
    