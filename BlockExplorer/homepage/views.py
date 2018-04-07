from django.shortcuts import render
# from django.Http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request, 'homepage/index.html')