from django.shortcuts import render
import requests
# from django.Http import HttpResponse
# Create your views here.


def homepage(request):
    a = requests.get("http://88.198.13.202:9051/blocks?offset=6&&limit=10")
    blocklist = a.json()
    # print(blocklist)
    return render(request, 'homepage/index.html', context={"blocklist": blocklist})
